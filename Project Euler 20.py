num = 100
times = 1
sum = 0
for i in range(1, num + 1):
    times *= i
for i in str(times):
    sum += int(i)
print(sum)