with open("input.txt") as file:
    data = [f.strip('\n') for f in file.readlines()]
# print(data)

ans = []


for s in data:
    stk = []
    n = len(s)
    k = n - 12
    for ch in s:
        # if (len(stk) == 0 or k == 0):
        #     stk.append(ch)
        # elif (ch > stk[-1]):
        #     stk.pop()
        #     stk.append(ch)
        #     k -= 1
        # elif (len(stk) <12):
        #     stk.append(ch)
        while k > 0 and stk and stk[-1] < ch:
            stk.pop()
            k -= 1
        stk.append(ch)
    # print(stk)
    if (k > 0):
        stk = stk[:-k]
    stk = stk[:12]
    ans.append(int(''.join(stk)))

print(sum(ans))