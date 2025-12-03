# from math import floor

with open("test.txt") as file:
    data = file.readlines()
data = [s.strip('\n') for s in data]

# print(data)
start_pos = 50
ans = 0

# for s in data:
#     rot = s[0]
#     num = int(s[1:])
#     if (rot == 'R'):
#         d = 100 if pos == 0 else 100 - pos
#         if (num >= d):
#             ans += 1 + (num - d)//100
#         pos = (pos + num)%100
#     else:
#         d = 100 if pos == 0 else pos
#         if (num >= d):
#             ans += 1 + (num - d)//100
#         pos = (pos - num)%100
# print(ans)

for s in data:
    rot = s[0]
    num = int(s[1:])
    mult = 1 if rot=='R' else -1
    end_pos = (start_pos + mult*num)%100
    if (rot == 'R'):
        d = 100 if start_pos == 0 else (100 - start_pos) #Dist from start to 0 in dir of movement
    elif (rot == 'L'):
        d = 100 if start_pos == 0 else start_pos
    if (num >= d):
        ans += 1 + (num - d)//100
    start_pos = end_pos
print(ans)  