sayilar = """3710...1690"""

sayi = sayilar.split("\n")
toplama = []
for i in sayi:
    i = int(i)
    toplama.append(i)
toplama = sum(toplama)
toplama = str(toplama)
num = toplama[0:10]

print(num)