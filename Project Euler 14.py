import time
def collatz(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1

def steps(x, known_steps):
    step = 0
    original_x = x
    path = []
    while x != 1:
        if x in known_steps:
            step += known_steps[x]
            break
        path.append(x)
        x = collatz(x)
        step += 1
    for index, value in enumerate(path):
        known_steps[value] = step - index
    return step
s = time.time()
max_step = 0
champ_number = 0
known_steps = {}

for i in range(1, 1000000):
    aux = steps(i, known_steps)
    if aux > max_step:
        max_step = aux
        champ_number = i
        print(f"Şu anki en yüksek adım sayısı: {max_step}, numara: {champ_number}")
f = time.time()
t = s - f
print(-t)
print("En uzun Collatz dizisini üreten sayı:", champ_number)
print("Adım sayısı:", max_step)