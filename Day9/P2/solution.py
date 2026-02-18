# from tqdm import tqdm

# with open("input.txt", "r") as f:
#     lines = [tuple(map(int, l.strip().split(','))) for l in f if l.strip()]

# poly = lines[:]           # polygon vertices in the given order
# n = len(poly)
# red_set = set(poly)

# # precompute polygon edges (axis-aligned segments)
# edges = []
# for i in range(n):
#     x1,y1 = poly[i]
#     x2,y2 = poly[(i+1) % n]
#     edges.append(((x1,y1),(x2,y2)))

# def point_on_edge(tx, ty):
#     """Return True if point (tx,ty) lies on any polygon edge (including vertices)."""
#     for (x1,y1),(x2,y2) in edges:
#         if x1 == x2:  # vertical edge
#             if tx == x1 and min(y1,y2) <= ty <= max(y1,y2):
#                 return True
#         elif y1 == y2:  # horizontal edge
#             if ty == y1 and min(x1,x2) <= tx <= max(x1,x2):
#                 return True
#         # else:
#         #     # polygon edges in this puzzle should be axis-aligned, but keep safe fallback
#         #     # check collinearity and bounding box
#         #     dx = x2 - x1
#         #     dy = y2 - y1
#         #     if dx * (ty - y1) == dy * (tx - x1) and min(x1,x2) <= tx <= max(x1,x2) and min(y1,y2) <= ty <= max(y1,y2):
#         #         return True
#     return False

# def point_in_poly(x, y, polygon):
#     """Ray-casting point-in-polygon. Returns True if strictly inside."""
#     inside = False
#     m = len(polygon)
#     for i in range(m):
#         x1,y1 = polygon[i]
#         x2,y2 = polygon[(i+1) % m]
#         # check edge crosses horizontal ray at y
#         if (y1 > y) != (y2 > y):
#             # safe because when y1==y2 condition is false
#             xinters = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
#             if x < xinters:
#                 inside = not inside
#     return inside

# ans = 0

# for i in tqdm(range(n)):
#     for j in range(i+1, n):
#         x1,y1 = poly[i]
#         x2,y2 = poly[j]
#         if x1 == x2 or y1 == y2:
#             continue  # need opposite corners (non-zero area)

#         xmin, xmax = sorted((x1,x2))
#         ymin, ymax = sorted((y1,y2))

#         # inclusive area (tiles are discrete and inclusive)
#         area = (xmax - xmin + 1) * (ymax - ymin + 1)

#         valid = True
#         # check every tile inside the rectangle
#         for tx in range(xmin, xmax + 1):
#             if not valid:
#                 break
#             for ty in range(ymin, ymax + 1):
#                 # the two opposite corners are red by construction
#                 if (tx,ty) == (x1,y1) or (tx,ty) == (x2,y2):
#                     continue
#                 # if tile is red it's allowed
#                 if (tx,ty) in red_set:
#                     continue
#                 # if tile lies exactly on polygon boundary (green) it's allowed
#                 if point_on_edge(tx, ty):
#                     continue
#                 # otherwise it must be strictly inside the polygon (green)
#                 if not point_in_poly(tx, ty, poly):
#                     valid = False
#                     break

#         if valid:
#             ans = max(ans, area)

# print(ans)


# Coordinate Compression + Flood fill
from collections import deque
from tqdm import tqdm

coords = []
with open("input.txt") as file:
    data = [line.strip() for line in file]

for line in data:
    coords.append(tuple(map(int, line.split(','))))

n = len(coords)

mapx = {}
mapy = {}
rmapx = {}
rmapy = {}

for idx, x in enumerate(sorted(set(c[0] for c in coords))):
    mapx[x] = idx*2
    rmapx[idx*2] = x

for idx, y in enumerate(sorted(set(c[1] for c in coords))):
    mapy[y] = idx*2
    rmapy[idx*2] = y

def look(i):
    return mapx[coords[i][0]], mapy[coords[i][1]]

filled = set()

for i in range(n):
    x1, y1 = look(i)
    x2, y2 = look((i+1)%n)
    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            filled.add((x1,y))
    if y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            filled.add((x,y1))

mx = my = 1e9
for i in range(n):
    x, y = look(i)
    mx = min(mx, x)

for i in range(n):
    x, y = look(i)
    if (x == mx):
        my = min(my, y)


directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}

dq = deque()
dq.append((mx + 1, my + 1))

while len(dq) > 0:
    x, y = dq.popleft()
    
    for dx,dy in directions:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in filled:
            filled.add((nx, ny))
            dq.append((nx, ny))

area = 0

for i in tqdm(range(n)):
    x1, y1 = look(i)
    for j in range(i + 1, n):
        x2, y2 = look(j)
        
        flag = True
        
        xmin, xmax = sorted((x1,x2))
        ymin, ymax = sorted((y1,y2))

        for x in range(xmin, xmax + 1):
            for y in [ymin, ymax]:
                if (x, y) not in filled:
                    flag = False
                    break
        
        for y in range(ymin, ymax + 1):
            for x in [xmin, xmax]:
                if (x, y) not in filled:
                    flag = False
                    break

        if flag:
            ox1 = rmapx[x1]
            ox2 = rmapx[x2]
            oy1 = rmapy[y1]
            oy2 = rmapy[y2]

            area = max(area, (abs(ox1 - ox2) + 1) * (abs(oy1 - oy2) + 1))

print(area)

