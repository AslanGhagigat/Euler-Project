alphabet = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

file = open("./p022_names.txt", "r")
a = file.readline()
names = a.split('","')
names[0] = names[0][1:]
names[-1] = names[-1][:-1]
names.sort()

answer = 0
count = 1
# name = 'COLIN'
for name in names:
    ans = 0
    for i in name:
        ans += alphabet[i]
    ans *= count
    count += 1
    answer += ans
# print(ans)
# print(names.index(name))
print(answer)
print(count)
