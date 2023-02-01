def prime(a):
    for i in range(2,a):
        if a%i==0:
            return ('not prime')
        else:
            return ('prime')
for x in range(600851475143):
    if(prime(600851475143))==('prime'):
        for i in range(2,600851475143):
            if 600851475143%i==0:
                print("for ",i," is not prime")
    else:
        for i in range(2,600851475143):
            if 600851475143%i==0:
                print("for ",i," is not prime")
#then we should see i is prime or not prime
