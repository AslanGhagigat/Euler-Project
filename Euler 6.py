num = 100
a = list(range(1,num + 1))
ans = sum(a) ** 2

for i in range(1,num + 1):
    ans -= i**2

print(ans)


#=================================
#======== A short program ========
#=================================
# ans , sum , num = 0 , 0 , 100
# for i in range(1,num + 1):
#     ans -= i**2
#     sum += i
# print(ans + sum**2)