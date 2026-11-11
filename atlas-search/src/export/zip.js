// Minimal streaming ZIP writer (STORE method, ZIP64-capable).
//
// Used to bundle an OME-Zarr store (whose chunks are already compressed)
// into a single downloadable .zip. Every entry is fully known before it is
// written, so CRC and sizes go straight into the local header and no data
// descriptors are needed.

const CRC_TABLE = (() => {
  const t = new Uint32Array(256);
  for (let n = 0; n < 256; n++) {
    let c = n;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    t[n] = c >>> 0;
  }
  return t;
})();

export function crc32(data, crc = 0) {
  let c = ~crc >>> 0;
  for (let i = 0; i < data.length; i++) c = CRC_TABLE[(c ^ data[i]) & 0xff] ^ (c >>> 8);
  return ~c >>> 0;
}

const U32_MAX = 0xffffffff;

function dosDateTime(d = new Date()) {
  const time = (d.getHours() << 11) | (d.getMinutes() << 5) | Math.floor(d.getSeconds() / 2);
  const date = ((d.getFullYear() - 1980) << 9) | ((d.getMonth() + 1) << 5) | d.getDate();
  return { time, date };
}

/**
 * @param {(chunk: Uint8Array) => Promise<void>} write sink
 */
export class ZipWriter {
  constructor(write) {
    this.write = write;
    this.offset = 0;
    this.entries = [];
    this.enc = new TextEncoder();
    this.dt = dosDateTime();
  }

  async _emit(bytes) {
    await this.write(bytes);
    this.offset += bytes.length;
  }

  /** Add a file. `data` is a Uint8Array (< 4 GiB). */
  async add(name, data) {
    const nameBytes = this.enc.encode(name);
    const crc = crc32(data);
    const size = data.length;
    const offset = this.offset;
    const h = new DataView(new ArrayBuffer(30));
    h.setUint32(0, 0x04034b50, true);
    h.setUint16(4, 45, true); // version needed (4.5 = zip64)
    h.setUint16(6, 0x0800, true); // UTF-8 names
    h.setUint16(8, 0, true); // STORE
    h.setUint16(10, this.dt.time, true);
    h.setUint16(12, this.dt.date, true);
    h.setUint32(14, crc, true);
    h.setUint32(18, size, true);
    h.setUint32(22, size, true);
    h.setUint16(26, nameBytes.length, true);
    h.setUint16(28, 0, true);
    await this._emit(new Uint8Array(h.buffer));
    await this._emit(nameBytes);
    if (size) await this._emit(data);
    this.entries.push({ nameBytes, crc, size, offset });
  }

  async close() {
    const cdStart = this.offset;
    for (const e of this.entries) {
      const big = e.offset >= U32_MAX;
      const extra = big ? 12 : 0;
      const h = new DataView(new ArrayBuffer(46 + extra));
      h.setUint32(0, 0x02014b50, true);
      h.setUint16(4, 45, true);
      h.setUint16(6, 45, true);
      h.setUint16(8, 0x0800, true);
      h.setUint16(10, 0, true);
      h.setUint16(12, this.dt.time, true);
      h.setUint16(14, this.dt.date, true);
      h.setUint32(16, e.crc, true);
      h.setUint32(20, e.size, true);
      h.setUint32(24, e.size, true);
      h.setUint16(28, e.nameBytes.length, true);
      h.setUint16(30, extra, true);
      h.setUint16(32, 0, true);
      h.setUint16(34, 0, true);
      h.setUint16(36, 0, true);
      h.setUint32(38, 0, true);
      h.setUint32(42, big ? U32_MAX : e.offset, true);
      if (big) {
        h.setUint16(46, 0x0001, true);
        h.setUint16(48, 8, true);
        h.setBigUint64(50, BigInt(e.offset), true);
      }
      // name goes between fixed header and extra field
      const fixed = new Uint8Array(h.buffer, 0, 46);
      await this._emit(fixed);
      await this._emit(e.nameBytes);
      if (big) await this._emit(new Uint8Array(h.buffer, 46, extra));
    }
    const cdSize = this.offset - cdStart;
    const n = this.entries.length;
    const needZip64 = n >= 0xffff || cdStart >= U32_MAX || cdSize >= U32_MAX;
    if (needZip64) {
      const z64Offset = this.offset;
      const r = new DataView(new ArrayBuffer(56 + 20));
      r.setUint32(0, 0x06064b50, true);
      r.setBigUint64(4, 44n, true);
      r.setUint16(12, 45, true);
      r.setUint16(14, 45, true);
      r.setUint32(16, 0, true);
      r.setUint32(20, 0, true);
      r.setBigUint64(24, BigInt(n), true);
      r.setBigUint64(32, BigInt(n), true);
      r.setBigUint64(40, BigInt(cdSize), true);
      r.setBigUint64(48, BigInt(cdStart), true);
      r.setUint32(56, 0x07064b50, true);
      r.setUint32(60, 0, true);
      r.setBigUint64(64, BigInt(z64Offset), true);
      r.setUint32(72, 1, true);
      await this._emit(new Uint8Array(r.buffer));
    }
    const e = new DataView(new ArrayBuffer(22));
    e.setUint32(0, 0x06054b50, true);
    e.setUint16(8, needZip64 ? 0xffff : n, true);
    e.setUint16(10, needZip64 ? 0xffff : n, true);
    e.setUint32(12, needZip64 ? U32_MAX : cdSize, true);
    e.setUint32(16, needZip64 ? U32_MAX : cdStart, true);
    await this._emit(new Uint8Array(e.buffer));
  }
}
