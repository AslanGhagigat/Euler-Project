num = 600851475143
last_div = 2
div_list = []
while num != 1:
    for i in range(last_div,num+1):
        if num % i == 0:
            num //= i
            last_div = i
            div_list.append(i)
            break

print(f"Last divisor is {last_div}\nand list of all divisors :\n{div_list}",sep="\n")
