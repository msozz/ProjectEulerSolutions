def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = 0
prime_list = []

while len(prime_list) < 10001:
    if is_prime(num):
        prime_list.append(num)
        num += 1
    else:
        num += 1

print(max(prime_list))