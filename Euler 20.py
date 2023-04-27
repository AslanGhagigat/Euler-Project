def Factorial(x: int):
    if x == 1:
        return x
    return x * Factorial(x-1)


def Sum_of_the_Digits(x: int):
    num = str(x)
    sumofthedigits = 0
    for i in num:
        sumofthedigits += int(i)
    return int(sumofthedigits)

n = 100

print(Sum_of_the_Digits(Factorial(n)))