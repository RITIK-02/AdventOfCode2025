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
# print(ranges)
# print(queries)

ans = 0
for q in queries:
    for r in ranges:
        idx = r.find('-')
        ll = int(r[:idx])
        ul = int(r[idx+1:])
        if (ll <= int(q) <= ul):
            ans += 1
            break
print(ans)
