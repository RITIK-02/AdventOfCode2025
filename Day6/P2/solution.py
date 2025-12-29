with open("input.txt") as file:
    data = file.readlines()

data = [d.strip('\n') for d in data]

m = len(data)
n = len(data[0])
ans = 0
arr = []
j = n - 1
while j >= 0:
    c = ""
    for i in range(m - 1):
        if (data[i][j] != ' '):
            c += data[i][j]
    arr.append(c)
    if (data[-1][j] != ' '):
        # print(arr)
        arr = [int(a) for a in arr]
        if data[-1][j] == '+':
            ans += sum(arr)
        else:
            res = 1
            for a in arr:
                res *= a
            ans += res
        arr = []
        j -= 1
    j -= 1
print(ans)