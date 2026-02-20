from collections import deque

with open("input.txt", "r") as f:
    inputs = [line.strip().split() for line in f.readlines()]

# BFS with XOR bitwise masking
ans = 0

def preprocess_target(t):
    mask = 0
    t = t[1:-1]
    for i,c in enumerate(t):
        if (c == '#'):
            mask |= (1 << i)
    return mask

def preprocess_power(p):
    p = p[1:-1]
    p = p.split(",")
    p = [int(x) for x in p]
    return p

def preprocess_wiring(w):
    masks = []
    for i in range(len(w)):
        bits = 0
        for d in w[i][1:-1].split(","):
            if d:
                bits |= (1 << int(d))
        masks.append(bits)
    return masks

def min_press(target, wiring):
    start = 0
    seen = {start}
    dq = deque([(start, 0)])

    while (len(dq) != 0):
        state, count = dq.popleft()

        if state == target:
            return count 
        
        for w in wiring:
            next_state = state ^ w

            if (next_state not in seen):
                seen.add(next_state)
                dq.append((next_state, count+1))
    
    return float("inf")

n = len(inputs)
for i in range(n):
    target = preprocess_target(inputs[i][0])
    power = preprocess_power(inputs[i][-1])
    wiring = preprocess_wiring(inputs[i][1:-1])
    ans += min_press(target, wiring)
    

print(ans)