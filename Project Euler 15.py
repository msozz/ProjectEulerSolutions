a = list()
for i in range(0, 21):
    for j in range(0, 21):
        a.append([i, j])

b = dict()
for i in range(1, 21):
    b[0, i] = 1
    b[i, 0] = 1
for i in range(1, 21):
    for j in range(1, 21):
        b[i, j] = 0
for i in range(1, 21):
    for j in range(1, 21):
        b[i, j] += b[i-1, j]
        b[i, j] += b[i, j-1]
print(b[20, 20])