c = 20
for X in range(20):
    t = 1
    v = 0
    if c%(X+1) != 0:
        v = X+1
        while True:
            t += 1
            if v%t == 0 and v not in (t, 1):
                v = t
            if (c*t)%(X+1) == 0:
                c *= v
                break
print(c)