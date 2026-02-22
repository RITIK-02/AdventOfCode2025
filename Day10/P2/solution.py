from scipy.optimize import milp, LinearConstraint
import numpy as np

with open("input.txt", "r") as f:
    inputs = [line.strip().split() for line in f.readlines()]

ans = 0

def preprocess_power(p):
    p = p[1:-1]
    p = p.split(",")
    p = [int(x) for x in p]
    return p

def preprocess_wiring(w):
    wiring = []
    for i in range(len(w)):
        wiring.append(tuple(map(int,w[i][1:-1].split(","))))
    return wiring

ans = 0

m = len(inputs)
for i in range(m):
    power = preprocess_power(inputs[i][-1])
    wiring = preprocess_wiring(inputs[i][1:-1])
    n = len(power)
    n2 = len(wiring)
    A = np.zeros((n, n2), dtype=int)

    for i in range(len(wiring)):
        for j in range(len(wiring[i])):
            A[wiring[i][j], i] = 1

    c = np.ones(n2, dtype=int)
    b = np.array(power)

    constraint = LinearConstraint(A, b, b)
    integrality = np.ones_like(c)
    res = milp(c=c, constraints=constraint, integrality=integrality)
    ans += sum(res.x)

print(int(ans))