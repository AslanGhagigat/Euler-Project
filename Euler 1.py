max_num = 1000                        # I enter maximum number but we can get the maximum number with this code :
                                      #          max_num = int(input()) 
sum_of_nums = 0                       # in this moment sum of numbers is equal 0  
for i in range(1,max_num):            # we have to check number in the range are multiple of 3 and 5 or not
    if i % 3 == 0 or i % 5 == 0:      # if number is multiple of 3 and 5 :
        sum_of_nums += i              # sum up multiple number with sum_of_nums
print(sum_of_nums)                    # print sum of multiple numbers
