def Is_palindromic(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

def div(x,pow):
    max_num = 10 ** pow -1
    min_num = 10 ** (pow-1)
    for i in range(max_num,min_num,-1):
        if (x%i == 0) and (min_num <= x//i <= max_num):
            return 1,i,x//i
    return 0

pow = 3
num = 10 ** (pow * 2)
for i in range(num,1,-1):
    if Is_palindromic(i) :
        ans = div(i,pow)
        if ans:
            print(i,*ans[1:])
            break

#=================================        
#======== A short program ========
#=================================        
# a = range(999,0,-1)
# adad = []
# for i in a:
#     for j in a:
#         x = str(i*j)
#         if x == x[::-1]:
#             adad.append(i*j)
# print(max(adad))