prime_factore = 100851475143
i = 2

while i * i < prime_factore:
    while prime_factore % i == 0:
       prime_factore = prime_factore/i
    i = i+1
    
print(prime_factore)