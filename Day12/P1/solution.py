import re

with open("input.txt") as file:
    blocks = []
    # print(file.readlines())
    blk = []
    for line in file.readlines():
        if (line == '\n'):
            blocks.append(blk)
            blk = []
            continue
        blk.append(line.strip('\n'))
    blocks.append(blk)
# print(blocks)

shapes = blocks[:-1]
shapes_bm = []
shapes_area = []
for sh in shapes:
    bits = ""
    for i in range(1,4):
        for j in range(3):
            bits += "1" if sh[i][j] == '#' else "0"
    b = int(bits, 2)
    shapes_bm.append(b)
    shapes_area.append(b.bit_count())

# print(shapes)
# print(shapes_area)
# print(bin(shapes_bm[0]))

ans = 0
# ard = []
for grid in blocks[-1]:
    num = list(map(int, re.findall(r"\d+", grid)))
    # print(num)
    row, col = num[:2]
    shapes_count = num[2:]

    tot_area = row*col
    area = 0
    for i in range(len(shapes)):
        area += shapes_count[i]*shapes_area[i]

    if (tot_area >= area):
        ans += 1
        # ard.append(tot_area - area)

# It seems that I just got lucky with this one
print(ans)
# print(sorted(ard))