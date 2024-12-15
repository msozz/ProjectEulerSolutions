def main():
    a = 1
    sum = 0
    divisors = 0

    while True:
        divisors = 0
        sum += a
        a += 1
        sqrt_sum = int(sum**0.5)

        for k in range(1, sqrt_sum+1):
            if sum % k == 0:
                divisors += 2

        if sqrt_sum * sqrt_sum == sum:  
            divisors -= 1

        if divisors > 500:
            break
    
    print(sum)

main()