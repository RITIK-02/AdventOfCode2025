with open("test.txt", "r") as file:
    inp = [f.rstrip('\n') for f in file.readlines()]

mat = []
for i in inp:
    row = []
    for ch in i:
        row.append(ch)
    mat.append(row)

# dir = [-1, 0, 1, 0]
ans = 0
m = len(mat)
n = len(mat[0])
for i in range(m):
    for j in range(n):
        count = 0
        if (mat[i][j] != '@'):
            continue
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x == 0 and y == 0):
                    continue
                if (0 <= i + x and i + x < m and 0 <= j + y and j + y < n):
                    if (mat[i+x][j+y] == '@'):
                        count += 1
        if (count < 4):
            ans += 1
print(ans)