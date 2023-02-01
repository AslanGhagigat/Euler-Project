max_num = 1000 
sum_of_nums = 0  
for i in range(1,max_num):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_nums += i
print(sum_of_nums)
