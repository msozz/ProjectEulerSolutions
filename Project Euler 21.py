sayi = 10000

def check(n):
    liste = []
    for i in range(1, n):
        if n % i == 0:
            liste.append(i)
    return sum(liste)

a = []
for i in range(2, sayi + 1):
    if i == check(check(i)):
        a.append(i)
    if i == check(i):
        a.remove(i)
print(sum(a))