from functools import lru_cache

with open("test.txt", "r") as f:
    inputs = [line.strip().split() for line in f.readlines()]

ans = 0

def preprocess_target(t):
    t = t[1:-1]
    t = list(t)
    t = [0 if x == "." else 1 for x in t]
    return t

def preprocess_power(p):
    p = p[1:-1]
    p = p.split(",")
    p = [int(x) for x in p]
    return p

def preprocess_wiring(w):
    wc = []
    for i in range(len(w)):
        wc.append(tuple(map(int, w[i][1:-1].split(","))))
    return wc

@lru_cache(None)
def dp(target, power, wiring, current):
    if (target == current):
        return 0
    mc = 1e9
    for w in wiring:
        for i in range(len(w)):
            current[w[i]] = not current[w[i]]
        c = dp(target, power, wiring, current) + 1
        mc = min(mc, c)
        for i in range(len(w)):
            current[w[i]] = not current[w[i]]

    return mc

n = len(inputs)
for i in range(n):
    target = preprocess_target(inputs[i][0])
    power = preprocess_power(inputs[i][-1])
    wiring = preprocess_wiring(inputs[i][1:-1])
    init = [0]*len(target)
    c = dp(target, power, wiring, init)
    ans += c

print(ans)