def Combination(x, y):
    def Factorial(x):
        if x == 1:
            return x
        return x * Factorial(x-1)
    return Factorial(x) // (Factorial(y) * Factorial(x-y))


row = 20
col = 20

print(Combination(row + col, min(row, col)))
