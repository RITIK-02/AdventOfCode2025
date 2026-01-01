with open("input.txt") as file:
    data = file.readlines()

mat = [d.rstrip('\n') for d in data]

m = len(mat)
n = len(mat[0])

start = -1
for j in range(n):
    if mat[0][j] == 'S':
        start = j

def func(mat, memo, prev, m, n, i):
    if (i >= m):
        return 1
    if memo.get((i, tuple(prev)), -1) != -1:
        return memo[(i, tuple(prev))]
    for j in range(n):
        if mat[i][j] == '^' and prev[j] == True:
            ans1 = 0
            ans2 = 0
            if (j > 0):
                prev[j] = False
                prev[j-1] = True
                ans1 = func(mat, memo, prev, m, n, i+2)
                prev[j-1] = False
                prev[j] = True
            if (j < n - 1):
                prev[j] = False
                prev[j+1] = True
                ans2 = func(mat, memo, prev, m, n, i+2)
                prev[j+1] = False
                prev[j] = True
            
            memo[(i, tuple(prev))] = ans1+ans2
            return ans1+ans2
        elif prev[j] == True:
            memo[(i, tuple(prev))] = func(mat, memo, prev, m, n, i+1)
            return memo[(i, tuple(prev))]
    return 0

def solution(mat, start, m, n):
    memo = {}
    prev = [False if j != start else True for j in range(n)]
    ans = func(mat, memo, prev, m, n, 2)
    return ans

ans = 0
ans = solution(mat, start, m, n)
print(ans)



# A more optimized solution
# from functools import lru_cache

# with open("input.txt") as f:
#     mat = [line.rstrip("\n") for line in f]

# m, n = len(mat), len(mat[0])

# # find start
# for j in range(n):
#     if mat[0][j] == "S":
#         start = j
#         break

# @lru_cache(None)
# def dp(i, j):
#     if j < 0 or j >= n:
#         return 0
#     if i >= m:
#         return 1

#     cell = mat[i][j]

#     if cell == '^':
#         return dp(i+2, j-1) + dp(i+2, j+1)
#     else:
#         # |, S, . all go straight
#         return dp(i+1, j)

# answer = dp(1, start)
# print(answer)
