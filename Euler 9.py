f = 0
for a in range(998,1,-1):
    if f == 1:
        break
    for b in range(1,999):
        if f == 1:
            break
        if ((10**6 + (2*a*b) - (2000*(a+b))) == 0) :
            print(a,b,(1000-(a+b)),a*b*(1000-(a+b)),sep='\t')
            f = 1
            break