names = sorted(["MARY",...,"BRODERICK","ALONSO"])

def fc(name):
    name = name.lower()
    sum = 0
    for i in name:
        cnum = ord(i) - ord('a') + 1
        sum += cnum
    return sum
top = 0
for name in names:
    top += fc(name)*(names.index(name) + 1)
print(top)