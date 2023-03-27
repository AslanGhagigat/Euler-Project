p = 2 * 10 ** 6
prime = 2

prime_list = [2]
for i in range(3,p+1):
    n = int((i**0.5)//1)+1
    for j in prime_list:
        if j > n:
            prime_list.append(i)
            prime += i
            break
        if i%j == 0:
            break
    else:
        prime_list.append(i)
        prime += i

print(prime,sep='\n')




