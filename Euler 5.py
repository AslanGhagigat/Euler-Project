def kmm(x,y):
    x1 = x
    y1 = y
    while(y):
        x, y = y, x%y
    bmm = x
    return (x1*y1)//bmm

KMM = 1
for i in range(1,21):
    KMM = kmm(KMM , i)

print('kmm: ',KMM)