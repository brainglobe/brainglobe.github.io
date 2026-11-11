// Output sinks: where exported bytes go.
//
// On Chromium browsers we use the File System Access API so multi-GB exports
// are streamed straight to disk. Elsewhere we collect parts into a Blob
// (browsers page large Blobs to disk, but memory use can still be high).

export const canStreamToDisk = typeof window !== "undefined" && "showSaveFilePicker" in window;

/**
 * Open a sink. MUST be called synchronously from a user gesture (click)
 * before any other `await`, otherwise the save dialog is blocked.
 * @returns {Promise<{write(u8: Uint8Array): Promise<void>, close(): Promise<void>, abort(): Promise<void>, streaming: boolean}>}
 */
export async function openSink(filename, { mimeType = "application/octet-stream", gzip = false } = {}) {
  let base;
  if (canStreamToDisk) {
    let handle;
    try {
      handle = await window.showSaveFilePicker({ suggestedName: filename });
    } catch (e) {
      if (e.name === "AbortError") throw e; // user cancelled
      handle = null; // e.g. blocked in an iframe: fall back to Blob
    }
    if (handle) base = await fileSink(handle);
  }
  if (!base) base = blobSink(filename, mimeType);
  return gzip ? gzipSink(base) : base;
}

async function fileSink(handle) {
  const ws = await handle.createWritable();
  return {
    streaming: true,
    write: (u8) => ws.write(u8),
    close: () => ws.close(),
    abort: () => ws.abort(),
  };
}

function blobSink(filename, mimeType) {
  const parts = [];
  return {
    streaming: false,
    async write(u8) {
      // copy: callers may reuse their buffers
      parts.push(new Blob([u8]));
    },
    async close() {
      const blob = new Blob(parts, { type: mimeType });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      setTimeout(() => URL.revokeObjectURL(url), 60_000);
    },
    async abort() {
      parts.length = 0;
    },
  };
}

/**
 * Wrap a sink so everything written is gzip-compressed (streaming).
 * With `closeInner: false`, closing finishes the gzip member but leaves the
 * inner sink open (used for NRRD: plain-text header, gzipped payload).
 */
export function gzipSink(inner, { closeInner = true } = {}) {
  const cs = new CompressionStream("gzip");
  const writer = cs.writable.getWriter();
  const reader = cs.readable.getReader();
  const pump = (async () => {
    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      await inner.write(value);
    }
  })();
  return {
    streaming: inner.streaming,
    async write(u8) {
      await writer.ready;
      await writer.write(u8);
    },
    async close() {
      await writer.close();
      await pump;
      if (closeInner) await inner.close();
    },
    async abort() {
      try {
        await writer.abort();
      } catch {
        /* ignore */
      }
      await inner.abort();
    },
  };
}
