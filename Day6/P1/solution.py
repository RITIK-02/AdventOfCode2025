with open("input.txt") as file:
    data = file.readlines()

data = [d.split() for d in data]
print(data)

m = len(data) - 1
n = len(data[0])

nums = data[:-1]
op = data[-1]
print(nums)
print(op)

ans = [0 if op[j] == '+' else 1 for j in range(n)]
for i in range(m):
    for j in range(n):
        if (op[j] == '+'):
            ans[j] += int(nums[i][j])
        else:
            ans[j] *= int(nums[i][j])
print(ans)
print(sum(ans))