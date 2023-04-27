filename = "p067_triangle.txt"
with open(filename) as f:
    data = f.readlines()

n = 100
a = []
for i in data:
    b = [int(c) for c in i.split()]
    a.append(b)
for i in range(n-1, -1, -1):
    for j in range(0, len(a[i])-1):
        a[i-1][j] += max(a[i][j], a[i][j+1])
print(a[0][0])
