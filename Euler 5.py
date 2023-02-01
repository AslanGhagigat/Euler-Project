from math import lcm
maxnum = int(input("please input maximum number: "))
kmm = 1
for i in range(1,maxnum+1):
    kmm = lcm(kmm,i)
print(kmm)
