n1 = 1
n2 = 2
result = 0
while (n1 <= 4000000):
    if n1 % 2 == 0:
        result += n1
    n1, n2 = n2, n1 + n2
print(result)