with open("test.txt") as file:
    data = file.readlines()

data = [tuple(map(int, reversed(f.rstrip('\n').split(',')))) for f in data]
# print(data)
max_area = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        a = abs(data[i][0] - data[j][0] + 1)
        b = abs(data[i][1] - data[j][1] + 1)
        area = a*b
        max_area = max(max_area, area)

print(max_area)