filename = "Euler 13 input file.txt"
with open(filename) as f:
    data = f.readlines()

sum = 0
for i in data:
    a = int(i)
    sum += a
print(str(sum)[:10])


# ============================================
# ===== can open file with different way =====
# ============================================
# infile = open(filename, 'r')
# data = infile.read()
# infile.close()
# def conter(data):
#     count = ''
#     for i in data:
#         if i == '\n':
#             print(count)
#             count = ''
#             continue
#         count += i
# conter(data)