with open("input.txt") as file:
    data = [f.strip('\n') for f in file.readlines()]
# print(data)

ans = 0

for s in data:
    max_num = -1
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if int(s[i]+s[j]) > max_num:
                max_num = int(s[i]+s[j])
    # print(max_num)
    ans += int(max_num)

print(ans)