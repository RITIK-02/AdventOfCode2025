with open('input.txt') as file:
    data = [f.split() for f in file.readlines()]

print(data)

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
for i in range(len(data)):
    adj_list[node_map[data[i][0][:-1]]] = [node_map[node] for node in data[i][1:]]

for i in range(len(node_map)):
    adj_list.setdefault(i, [])
print(adj_list)

ans = [0]

def dfs(adj_list, visited, node, dest, count):
    if (node == dest):
        count[0] += 1
        return

    visited[node] = True
    for neigh in adj_list[node]:
        if (not visited[neigh]):
            dfs(adj_list, visited, neigh, dest, count)
    
    visited[node] = False

visited = [False]*len(node_map)

dfs(adj_list, visited, node_map["you"], node_map["out"], ans)

print(ans[0])