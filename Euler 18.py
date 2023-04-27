n = 15
a = []
for i in range(1,n+1):
    inp = input().split()
    b = [int(c) for c in inp]
    a.append(b)

for i in range(n-1,-1,-1):
    for j in range(0,len(a[i])-1):
        a[i-1][j] += max(a[i][j],a[i][j+1])
print(a[0][0])