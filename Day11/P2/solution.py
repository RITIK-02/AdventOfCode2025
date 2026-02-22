from collections import deque

with open('test.txt') as file:
    data = [f.split() for f in file.readlines()]

# print(data)

node_map = {}
rev_node_map = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        node = data[i][j]
        node = node.strip(":")
        if (node not in node_map):
            ind = len(node_map)
            node_map[node] = ind
            rev_node_map[ind] = node

adj_list = {}
indegree = [0]*len(node_map)


for i in range(len(data)):
    adj_list[node_map[data[i][0][:-1]]] = [node_map[node] for node in data[i][1:]]
    for n in adj_list[node_map[data[i][0][:-1]]]:
        indegree[n] += 1 

for i in range(len(node_map)):
    adj_list.setdefault(i, [])
# print(adj_list)

#DFS has complexity 2^n
#Topological sort traversal
q = deque()
for i in range(len(node_map)):
    if indegree[i] == 0:
        q.append(i)

topo = []
while (q):
    node = q.popleft()
    topo.append(node)

    for neigh in adj_list[node]:
        indegree[neigh] -= 1
        if (indegree[neigh] == 0):
            q.append(neigh)

# print(topo)
if len(topo) != len(node_map):
    print("Graph has a cycle!")
else:
    print("No cycles")

# #Only for paths with no constraints
# paths = [0] * len(node_map)
# paths[node_map["svr"]] = 1
# for node in topo:
#     for neigh in adj_list[node]:
#         paths[neigh] += paths[node]
# print(paths[node_map["out"]])

paths = [[0]*4 for _ in range(len(node_map))]

START = node_map["svr"]
DAC = node_map["dac"]
FFT = node_map["fft"]
DEST = node_map["out"]

# 4 masks, 0 -> START, 1 -> DAC, 2 -> FFT, 3 -> DAC & FFT
mask = 0
if (START == DAC):
    mask |= 1
if (START == FFT):
    mask |= 2
paths[START][mask] = 1

for node in topo:
    for mask in range(4):
        if paths[node][mask] == 0:
            continue
        for neigh in adj_list[node]:
            new_mask = mask
            if neigh == DAC:
                new_mask |= 1
            if neigh == FFT:
                new_mask |= 2
            paths[neigh][new_mask] += paths[node][mask]

print(paths[DEST][3])