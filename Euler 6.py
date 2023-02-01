sum=0
paye=0
for i in range(101):
    sum=sum+i
    #print(pow(i,2))
    paye=paye+pow(i,2)
a=(pow(sum,2))
b=(paye)
if a>b:
    print(a-b)
else:
    print(b-a)
