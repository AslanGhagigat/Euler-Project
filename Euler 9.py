def etehad(a,b,c):
    if a<b<c and (a+b+c)==1000 and (a**2)+(b**2)==(c**2) :
        return True
for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            if (etehad(a,b,c)):
                print(a,b,c,a*b*c)
                break
print('Finish')
