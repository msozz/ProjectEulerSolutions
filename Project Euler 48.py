a = 1
sum = 0
while a < 1001:
    sum += a**a
    a += 1
sum = str(sum)
print(sum[-10:-1]+sum[-1])