def Is_Prime(x):
    for i in range(2,int((x**0.5)//1)+1):
        if x%i == 0:
            return False
    return True


count = 0
num = 1
while count != 10001:
    num += 1
    if Is_Prime(num):
        count += 1
    
print(num)

