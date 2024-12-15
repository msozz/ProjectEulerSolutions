def prime(x):
    flag=True
    for i in range(2,int(x**0.5+1),1):
        if (x%i==0):
            flag=False
            break
        else:
            continue
    return flag

sum=0 
for i in range(2,2000001,1):
    if (prime(i)):
        sum+=i
    else:
        continue
print(sum)