with open("input.txt") as file:
    data = file.readlines()[0].split(',')
# print(data)

ans = []

for inp in data:
    lr = inp.split('-')[0]
    hr = inp.split('-')[1]
    # print(lr, hr)
    if (len(lr)%2 != 0 and len(hr)%2 != 0):
        continue
    for i in range(int(lr), int(hr) + 1):
        str_i = str(i)
        len_i = len(str_i)
        if (len_i%2 != 0):
            continue
        for j in range(len_i//2, len_i):
            if (str_i[j - len_i//2] != str_i[j]):
                break
        else:
            # print(i)
            ans.append(i)

print(sum(ans))
