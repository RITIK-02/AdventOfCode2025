with open("input.txt") as file:
    data = file.readlines()[0].split(',')
# print(data)

ans = set()

for inp in data:
    lr = inp.split('-')[0]
    hr = inp.split('-')[1]
    # print(lr, hr)
    for i in range(int(lr), int(hr) + 1):
        str_i = str(i)
        len_i = len(str_i)
        s = ""
        for ch in str_i:
            s += ch
            len_s = len(s)
            if (int(len_i/len_s) != len_i/len_s or int(len_i/len_s) == 1):
                continue
            if (str_i == s*int(len_i/len_s)):
                # print(str_i, "==", s*int(len_i/len_s))
                ans.add(i)
                
# print(ans)
print(sum(ans))
