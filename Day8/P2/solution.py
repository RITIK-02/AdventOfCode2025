from math import sqrt
import numpy as np

with open("input.txt") as file:
    data = [line.rstrip('\n') for line in file.readlines()]

coordi = [c.split(',') for c in data]
coordi = [(int(c[0]), int(c[1]), int(c[2])) for c in coordi]

def euclid_dist(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1]*size
    
    def find(self, i):
        root = self.parent[i]
        if self.parent[root] != root:
            self.parent[i] = self.find(root)
            return self.parent[i]
        return root

    def unionBySize(self, i, j):
        ip = self.find(i)
        jp = self.find(j)

        if ip == jp:
            return
        
        isize = self.size[ip]
        jsize = self.size[jp]

        if (isize < jsize):
            self.parent[ip] = jp
            self.size[jp] += isize
        else:
            self.parent[jp] = ip
            self.size[ip] += jsize

clusters = UnionFind(len(coordi))
dist = []
for i in range(len(coordi)):
    for j in range(i + 1, len(coordi)):
        dist.append((euclid_dist(coordi[i], coordi[j]), (i, j)))
dist2 = sorted(dist)

for d, (i, j) in dist2:
    clusters.unionBySize(i, j)
    c = np.array(clusters.size)
    idx = np.argmax(c)
    if (c[idx] == len(coordi)):
        print(coordi[i][0] * coordi[j][0])
        break

# cc = []
# for pt in range(len(coordi)):
#     if (clusters.parent[pt] == pt):
#         cc.append(clusters.size[pt])

# cc.sort(reverse=True)
# print(cc[0]*cc[1]*cc[2])
