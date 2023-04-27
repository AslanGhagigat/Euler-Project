global prime_list
prime_list = [2]


def Is_Prime(x):
    root = int(x**0.5)+1
    for i in prime_list:
        if x % i == 0:
            return False
        if i > root:
            break
    prime_list.append(x)
    return True


longest_chain = 1
longest_chain_num = 0

for i in range(3, 10**6):
    Is_Prime(i)

for i in prime_list[::-1]:
    a, b = 0, longest_chain
    while prime_list[b] < i:
        chain = b-a
        if chain < longest_chain:
            break
        if sum(prime_list[a:b]) == i:
            if chain > longest_chain:
                longest_chain = chain
                longest_chain_num = i
            break
        elif sum(prime_list[a:b]) > i:
            a += 1
            if a == b:
                break
            continue
        elif sum(prime_list[a:b]) < i:
            b += 1
            continue

print(longest_chain, longest_chain_num)
