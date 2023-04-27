a = 0
n = 1000
for i in range(1,n+1):
    a += i ** i
print(str(a)[-10:])