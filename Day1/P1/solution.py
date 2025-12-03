with open("input.txt") as file:
    data = file.readlines()
data = [s.strip('\n') for s in data]

# print(data)
pos = 50
ans = 0
for s in data:
    rot = s[0]
    num = int(s[1:])
    mult = 1 if rot=='R' else -1
    pos = (pos + mult*num)%100
    if pos == 0:
        ans += 1
print(ans)