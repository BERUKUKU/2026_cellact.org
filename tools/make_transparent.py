"""Turn the supplied logo (grey on off-white) into a transparent PNG using only the stdlib."""
import zlib, struct, sys
src, dst = sys.argv[1], sys.argv[2]
HEX = sys.argv[3] if len(sys.argv) > 3 else '6A6562'  # output logo colour
d = open(src, 'rb').read()
assert d[:8] == b'\x89PNG\r\n\x1a\n'
pos, idat, ihdr = 8, b'', None
while pos < len(d):
    n, t = struct.unpack('>I4s', d[pos:pos+8]); body = d[pos+8:pos+8+n]; pos += 12 + n
    if t == b'IHDR': ihdr = struct.unpack('>IIBBBBB', body)
    elif t == b'IDAT': idat += body
w, h, depth, ctype, _, _, inter = ihdr
assert depth == 8 and ctype == 6 and inter == 0, ihdr
bpp, stride = 4, w * 4
raw = zlib.decompress(idat)
rows, prev = [], bytearray(stride)
i = 0
for _ in range(h):
    f = raw[i]; line = bytearray(raw[i+1:i+1+stride]); i += 1 + stride
    for x in range(stride):
        a = line[x-bpp] if x >= bpp else 0; b = prev[x]; c = prev[x-bpp] if x >= bpp else 0
        if f == 1: line[x] = (line[x] + a) & 255
        elif f == 2: line[x] = (line[x] + b) & 255
        elif f == 3: line[x] = (line[x] + ((a + b) >> 1)) & 255
        elif f == 4:
            p = a + b - c; pa, pb, pc = abs(p-a), abs(p-b), abs(p-c)
            line[x] = (line[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
    rows.append(line); prev = line
# luminance over white
def lum(px):
    r, g, b, a = px; l = (r + g + b) / 3
    return 255 - (255 - l) * (a / 255)
lums = sorted(lum(rows[y][x*4:x*4+4]) for y in range(0, h, 3) for x in range(0, w, 3))
ink = lums[int(len(lums) * 0.02)]            # darkest 2% ~ solid logo colour
bg = lums[int(len(lums) * 0.97)]             # near-white background
print('ink', ink, 'bg', bg)
col = tuple(int(HEX[i:i+2], 16) for i in (0, 2, 4))
out = bytearray()
for line in rows:
    out.append(0)
    for x in range(w):
        l = lum(line[x*4:x*4+4])
        a = max(0.0, min(1.0, (bg - l) / (bg - ink)))
        if a < 0.04: a = 0.0
        out += bytes((col[0], col[1], col[2], round(a * 255)))
png = b'\x89PNG\r\n\x1a\n'
def chunk(t, b): return struct.pack('>I', len(b)) + t + b + struct.pack('>I', zlib.crc32(t + b) & 0xffffffff)
png += chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(bytes(out), 9)) + chunk(b'IEND', b'')
open(dst, 'wb').write(png)
