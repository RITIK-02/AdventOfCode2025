from tqdm import tqdm

with open("input.txt") as file:
    data = [f.strip('\n') for f in file.readlines()]
# print(data)

ans = 0

for s in tqdm(data):
    max_num = -1
    num = 0
    for i in range(len(s)):
        for i2 in range(i + 1, len(s)):
            for i3 in range(i2+1, len(s)):
                for i4 in range(i3+1, len(s)):
                    for i5 in range(i4+1, len(s)):
                        for i6 in range(i5+1, len(s)):
                            for i7 in range(i6+1, len(s)):
                                for i8 in range(i7+1, len(s)):
                                    for i9 in range(i8+1, len(s)):
                                        for i10 in range(i9+1, len(s)):
                                            for i11 in range(i10+1, len(s)):
                                                for i12 in range(i11+1, len(s)):
                                                    num = int(s[i]+s[i2]+s[i3]+s[i4]+s[i5]+s[i6]+s[i7]+s[i8]+s[i9]+s[i10]+s[i11]+s[i12])
                                                    if num > max_num:
                                                        max_num = num
    # print(max_num)
    ans += int(max_num)

print(ans)