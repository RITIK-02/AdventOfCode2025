with open("input.txt") as file:
    data = file.readlines()

mat = [d.strip('\n') for d in data]

m = len(mat)
n = len(mat[0])

start = -1
for j in range(n):
    if mat[0][j] == 'S':
        start = j

ans = 0
prev = [False if j != start else True for j in range(n)]
for i in range(2, m-1):
    for j in range(n):
        if mat[i][j] == '^' and prev[j] == True:
            ans += 1
            prev[j] = False
            if (j > 0):
                prev[j-1] = True
            if (j < n - 1):
                prev[j+1] = True
print(ans)