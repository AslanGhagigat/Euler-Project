x=int(input('please input your maximum number: '))
def is_prime(i):
    aval=True
    for n in range(2,i):
        if i % n ==0:
            aval=False
            break
    return aval
prime_sum=0
last_prime=0
for i in range(1,x+1):
    if (is_prime(i)):
        prime_sum=prime_sum+1
        #prime_sum=i
        if prime_sum==x:
            print(i)
