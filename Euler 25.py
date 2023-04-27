a = 1
b = 1
count = 1
while len(str(a)) < 10**3:
    a, b = b, a+b
    count += 1

print(count)
