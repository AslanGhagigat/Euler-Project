def divisors(x):
    div = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            div += 2
    if (x ** 0.5) % 1 != 0:
        return div
    else:
        return div - 1


triangle_number = 1
step = 2
while divisors(triangle_number) < 500:
    triangle_number += step
    step += 1
print(triangle_number, divisors(triangle_number))
