def is_prime(n):
    aval=True
    for i in range(2,int((n**0.5)+1)):
        if n % i ==0:
            aval=False
            break
    return aval

p=int(input('please input your maximum number: '))
prime=[]

for i in range(2,p+1):
    if (is_prime(i)):
        prime.append(i)
print(sum(prime))
