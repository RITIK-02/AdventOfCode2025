with open("input.txt", "r") as file:
    data = [f.rstrip('\n') for f in file.readlines()]

# print(data)

midx = None
for i in range(len(data)):
    if (data[i] == ''):
        midx = i
        break

ranges = data[:i]
queries = data[i + 1:]
ranges2 = []
for r in ranges:
    idx = r.find('-')
    ll = int(r[:idx])
    ul = int(r[idx+1:])
    ranges2.append((ll, ul))

ranges2 = sorted(ranges2)

print(ranges2)

fr = []
fr.append(ranges2[0])
for i in range(1, len(ranges2)):
    if (fr[-1][1] >= ranges2[i][0]):
        ll = fr[-1][0]
        ul = max(fr[-1][1], ranges2[i][1])
        fr.pop()
    else:
        ll = ranges2[i][0]
        ul = ranges2[i][1]
    fr.append((ll, ul))

print(fr)
ans = 0
for r in fr:
    ans += r[1] - r[0] + 1

print(ans)
