// Header writers for the volume export formats.
//
// All three formats (TIFF, NIfTI-1, NRRD) are written as
//     <header bytes> + <raw little-endian voxel data in C order (z, y, x)>
// so a volume can be streamed to disk slab by slab without ever holding
// the whole array in memory. Each writer only needs to produce the header.
//
// BrainGlobe arrays are stored with axes (z, y, x) in C order, so the
// fastest-varying axis on disk is x. NIfTI and NRRD list axes fastest-first,
// so their axis i corresponds to array axis 2 (x), j to 1 (y), k to 0 (z).

export const DTYPES = {
  uint8: { bytes: 1, tiffFormat: 1, nifti: 2, nrrd: "uint8" },
  int8: { bytes: 1, tiffFormat: 2, nifti: 256, nrrd: "int8" },
  uint16: { bytes: 2, tiffFormat: 1, nifti: 512, nrrd: "uint16" },
  int16: { bytes: 2, tiffFormat: 2, nifti: 4, nrrd: "int16" },
  uint32: { bytes: 4, tiffFormat: 1, nifti: 768, nrrd: "uint32" },
  int32: { bytes: 4, tiffFormat: 2, nifti: 8, nrrd: "int32" },
  float32: { bytes: 4, tiffFormat: 3, nifti: 16, nrrd: "float" },
  float64: { bytes: 8, tiffFormat: 3, nifti: 64, nrrd: "double" },
};

function dtypeInfo(dtype) {
  const d = DTYPES[dtype];
  if (!d) throw new Error(`Unsupported data type: ${dtype}`);
  return d;
}

// ---------------------------------------------------------------------------
// Orientation
// ---------------------------------------------------------------------------
// BrainGlobe orientation strings give the *origin* of each array axis, e.g.
// "asr" = axis 0 starts Anterior (increases towards posterior), axis 1 starts
// Superior, axis 2 starts Right. Returns, for each array axis, the unit
// direction of increasing index in RAS+ world space.
const AXIS_DIRECTION = {
  a: [0, -1, 0], p: [0, 1, 0],
  s: [0, 0, -1], i: [0, 0, 1],
  r: [-1, 0, 0], l: [1, 0, 0],
};

export function rasDirections(orientation = "asr") {
  const o = orientation.toLowerCase();
  const family = (c) => "ap si rl".split(" ").findIndex((f) => f.includes(c));
  if (
    o.length !== 3 ||
    [...o].some((c) => !AXIS_DIRECTION[c]) ||
    new Set([...o].map(family)).size !== 3
  ) {
    throw new Error(`Invalid orientation: ${orientation}`);
  }
  return [...o].map((c) => AXIS_DIRECTION[c]);
}

/**
 * 4x4 voxel->RAS(mm) affine for NIfTI/NRRD axes (i, j, k) = array (x, y, z).
 * @param {number[]} spacingZYX voxel size in mm, array axis order
 * @param {string} orientation BrainGlobe orientation string
 */
export function rasAffine(spacingZYX, orientation) {
  const dirs = rasDirections(orientation); // per array axis z, y, x
  const ijk = [2, 1, 0]; // nifti axis -> array axis
  const A = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
  ];
  ijk.forEach((arrAxis, col) => {
    for (let row = 0; row < 3; row++) {
      A[row][col] = dirs[arrAxis][row] * spacingZYX[arrAxis];
    }
  });
  return A;
}

// ---------------------------------------------------------------------------
// NIfTI-1
// ---------------------------------------------------------------------------
function quaternFromRotation(R) {
  // R: 3x3 proper rotation (det = +1). Port of nifti_mat44_to_quatern.
  const [[r11, r12, r13], [r21, r22, r23], [r31, r32, r33]] = R;
  let a = r11 + r22 + r33 + 1.0;
  let b, c, d;
  if (a > 0.5) {
    a = 0.5 * Math.sqrt(a);
    b = (0.25 * (r32 - r23)) / a;
    c = (0.25 * (r13 - r31)) / a;
    d = (0.25 * (r21 - r12)) / a;
  } else {
    const xd = 1.0 + r11 - (r22 + r33);
    const yd = 1.0 + r22 - (r11 + r33);
    const zd = 1.0 + r33 - (r11 + r22);
    if (xd > 1.0) {
      b = 0.5 * Math.sqrt(xd);
      c = (0.25 * (r12 + r21)) / b;
      d = (0.25 * (r13 + r31)) / b;
      a = (0.25 * (r32 - r23)) / b;
    } else if (yd > 1.0) {
      c = 0.5 * Math.sqrt(yd);
      b = (0.25 * (r12 + r21)) / c;
      d = (0.25 * (r23 + r32)) / c;
      a = (0.25 * (r13 - r31)) / c;
    } else {
      d = 0.5 * Math.sqrt(zd);
      b = (0.25 * (r13 + r31)) / d;
      c = (0.25 * (r23 + r32)) / d;
      a = (0.25 * (r21 - r12)) / d;
    }
    if (a < 0) {
      b = -b;
      c = -c;
      d = -d;
    }
  }
  return [b, c, d];
}

function det3(m) {
  return (
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
    m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
    m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
  );
}

/**
 * Build a 352-byte NIfTI-1 single-file (.nii) header.
 * @param {object} p
 * @param {number[]} p.shape array shape (z, y, x)
 * @param {string} p.dtype zarr data type name
 * @param {number[]} p.spacing voxel size in mm, (z, y, x)
 * @param {string} p.orientation BrainGlobe orientation string
 * @param {string} [p.description]
 */
export function niftiHeader({ shape, dtype, spacing, orientation, description = "" }) {
  const info = dtypeInfo(dtype);
  const buf = new ArrayBuffer(352);
  const v = new DataView(buf);
  const u8 = new Uint8Array(buf);
  const LE = true;
  v.setInt32(0, 348, LE);
  u8[38] = "r".charCodeAt(0);
  const [nz, ny, nx] = shape;
  const dims = [3, nx, ny, nz, 1, 1, 1, 1];
  dims.forEach((d, i) => v.setInt16(40 + 2 * i, d, LE));
  v.setInt16(70, info.nifti, LE);
  v.setInt16(72, info.bytes * 8, LE);

  // Rotation part of the affine (unit columns) to derive the quaternion.
  const A = rasAffine(spacing, orientation);
  const pix = [spacing[2], spacing[1], spacing[0]];
  const R = [0, 1, 2].map((r) => [0, 1, 2].map((c) => A[r][c] / pix[c]));
  let qfac = 1;
  if (det3(R) < 0) {
    qfac = -1;
    for (let r = 0; r < 3; r++) R[r][2] = -R[r][2];
  }
  const [qb, qc, qd] = quaternFromRotation(R);

  const pixdim = [qfac, pix[0], pix[1], pix[2], 1, 1, 1, 1];
  pixdim.forEach((p, i) => v.setFloat32(76 + 4 * i, p, LE));
  v.setFloat32(108, 352, LE); // vox_offset
  v.setFloat32(112, 1, LE); // scl_slope
  v.setFloat32(116, 0, LE); // scl_inter
  u8[123] = 2; // xyzt_units: NIFTI_UNITS_MM
  const desc = new TextEncoder().encode(description.slice(0, 79));
  u8.set(desc, 148);
  v.setInt16(252, 1, LE); // qform_code: scanner anat
  v.setInt16(254, 1, LE); // sform_code: scanner anat
  v.setFloat32(256, qb, LE);
  v.setFloat32(260, qc, LE);
  v.setFloat32(264, qd, LE);
  v.setFloat32(268, A[0][3], LE);
  v.setFloat32(272, A[1][3], LE);
  v.setFloat32(276, A[2][3], LE);
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 4; c++) v.setFloat32(280 + 16 * r + 4 * c, A[r][c], LE);
  }
  u8.set([0x6e, 0x2b, 0x31, 0x00], 344); // "n+1\0"
  // bytes 348..351: extension flag = 0 (no extensions)
  return u8;
}

// ---------------------------------------------------------------------------
// NRRD
// ---------------------------------------------------------------------------
export function nrrdHeader({ shape, dtype, spacing, orientation, gzip = false, description = "" }) {
  const info = dtypeInfo(dtype);
  const A = rasAffine(spacing, orientation);
  const [nz, ny, nx] = shape;
  const vec = (c) => `(${[0, 1, 2].map((r) => fmt(A[r][c])).join(",")})`;
  const lines = [
    "NRRD0004",
    "# Complete NRRD file format specification at:",
    "# http://teem.sourceforge.net/nrrd/format.html",
    ...(description ? [`# ${description.replace(/\n/g, " ")}`] : []),
    `type: ${info.nrrd}`,
    "dimension: 3",
    "space: right-anterior-superior",
    `sizes: ${nx} ${ny} ${nz}`,
    `space directions: ${vec(0)} ${vec(1)} ${vec(2)}`,
    "kinds: domain domain domain",
    ...(info.bytes > 1 ? ["endian: little"] : []),
    `encoding: ${gzip ? "gzip" : "raw"}`,
    "space origin: (0,0,0)",
    'space units: "mm" "mm" "mm"',
    "",
    "",
  ];
  return new TextEncoder().encode(lines.join("\n"));
}

function fmt(x) {
  // compact, exact-enough decimal (avoid -0 and float noise)
  if (Object.is(x, -0) || x === 0) return "0";
  return String(Number(x.toPrecision(12)));
}

// ---------------------------------------------------------------------------
// TIFF / BigTIFF (multi-page, uncompressed, one strip per page)
// ---------------------------------------------------------------------------
const T_ASCII = 2, T_SHORT = 3, T_LONG = 4, T_RATIONAL = 5, T_LONG8 = 16;

/**
 * Build the header (file header + all IFDs) for a multi-page TIFF whose
 * pixel data for page z starts immediately after the header, page after page.
 * Uses BigTIFF automatically when the file would exceed 4 GiB.
 * @param {object} p
 * @param {number[]} p.shape (z, y, x)
 * @param {string} p.dtype
 * @param {number[]} p.spacing voxel size in mm (z, y, x)
 * @param {string} [p.description] free text appended to image metadata
 * @param {boolean} [p.forceBigTiff]
 */
export function tiffHeader({ shape, dtype, spacing, forceBigTiff = false }) {
  const info = dtypeInfo(dtype);
  const [nz, ny, nx] = shape;
  const planeBytes = nx * ny * info.bytes;
  const dataBytes = planeBytes * nz;

  // ImageJ hyperstack description for types ImageJ understands; otherwise a
  // tifffile "shaped" JSON description. Both are read as a 3D stack by
  // tifffile (used throughout BrainGlobe) and as a stack by Fiji.
  const um = spacing.map((s) => s * 1000);
  const imagejOk = ["uint8", "uint16", "float32"].includes(dtype);
  const desc = imagejOk
    ? `ImageJ=1.11a\nimages=${nz}\nslices=${nz}\nunit=micron\nspacing=${fmt(um[0])}\nloop=false\n\0`
    : `${JSON.stringify({ shape: [nz, ny, nx] })}\0`;
  const descBytes = new TextEncoder().encode(desc);

  const xres = rational(1 / um[2]);
  const yres = rational(1 / um[1]);

  const estimateClassic = 8 + nz * (2 + 14 * 12 + 4 + 16) + descBytes.length + dataBytes;
  const big = forceBigTiff || estimateClassic >= 2 ** 32 - 1;

  const nTags = 14; // page 0 has ImageDescription; others 13
  const entrySize = big ? 20 : 12;
  const ifdSize = (n) => (big ? 8 + n * entrySize + 8 : 2 + n * entrySize + 4);
  const extraPerPage = 16; // two rationals stored out of line
  const headerSize = big ? 16 : 8;

  // layout: header | [IFD_z, extra_z] * nz | description | pixel data
  const pageBlock = (z) => ifdSize(z === 0 ? nTags : nTags - 1) + extraPerPage;
  let total = headerSize;
  const ifdOffsets = [];
  for (let z = 0; z < nz; z++) {
    ifdOffsets.push(total);
    total += pageBlock(z);
  }
  const descOffset = total;
  total += descBytes.length;
  if (total % 2) total += 1; // word-align pixel data
  const dataOffset = total;

  const buf = new ArrayBuffer(dataOffset);
  const v = new DataView(buf);
  const u8 = new Uint8Array(buf);
  const LE = true;
  v.setUint16(0, 0x4949, LE); // "II"
  if (big) {
    v.setUint16(2, 43, LE);
    v.setUint16(4, 8, LE);
    v.setUint16(6, 0, LE);
    v.setBigUint64(8, BigInt(ifdOffsets[0]), LE);
  } else {
    v.setUint16(2, 42, LE);
    v.setUint32(4, ifdOffsets[0], LE);
  }
  u8.set(descBytes, descOffset);

  for (let z = 0; z < nz; z++) {
    const off = ifdOffsets[z];
    const n = z === 0 ? nTags : nTags - 1;
    const extra = off + ifdSize(n);
    v.setUint32(extra, xres[0], LE);
    v.setUint32(extra + 4, xres[1], LE);
    v.setUint32(extra + 8, yres[0], LE);
    v.setUint32(extra + 12, yres[1], LE);
    const stripOffset = dataOffset + z * planeBytes;
    const entries = [
      [256, T_LONG, 1, nx],
      [257, T_LONG, 1, ny],
      [258, T_SHORT, 1, info.bytes * 8],
      [259, T_SHORT, 1, 1],
      [262, T_SHORT, 1, 1],
      ...(z === 0 ? [[270, T_ASCII, descBytes.length, descOffset]] : []),
      [273, big ? T_LONG8 : T_LONG, 1, stripOffset],
      [277, T_SHORT, 1, 1],
      [278, T_LONG, 1, ny],
      [279, big ? T_LONG8 : T_LONG, 1, planeBytes],
      [282, T_RATIONAL, 1, extra],
      [283, T_RATIONAL, 1, extra + 8],
      [296, T_SHORT, 1, 1],
      [339, T_SHORT, 1, info.tiffFormat],
    ];
    let p = off;
    if (big) {
      v.setBigUint64(p, BigInt(entries.length), LE);
      p += 8;
    } else {
      v.setUint16(p, entries.length, LE);
      p += 2;
    }
    for (const [tag, type, count, value] of entries) {
      v.setUint16(p, tag, LE);
      v.setUint16(p + 2, type, LE);
      if (big) {
        v.setBigUint64(p + 4, BigInt(count), LE);
        if (type === T_SHORT) v.setUint16(p + 12, value, LE);
        else if (type === T_LONG) v.setUint32(p + 12, value, LE);
        else v.setBigUint64(p + 12, BigInt(value), LE);
        p += 20;
      } else {
        v.setUint32(p + 4, count, LE);
        if (type === T_SHORT) v.setUint16(p + 8, value, LE);
        else v.setUint32(p + 8, value, LE);
        p += 12;
      }
    }
    const next = z + 1 < nz ? ifdOffsets[z + 1] : 0;
    if (big) v.setBigUint64(p, BigInt(next), LE);
    else v.setUint32(p, next, LE);
  }
  return u8;
}

function rational(x) {
  // approximate a positive float as a ratio of uint32s
  const den = 1000000;
  return [Math.round(x * den), den];
}

/** Total output size in bytes for a raw (uncompressed) export. */
export function rawSize(shape, dtype) {
  return shape.reduce((a, b) => a * b, 1) * dtypeInfo(dtype).bytes;
}
