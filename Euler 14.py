global chain_list

def Collatz(x):
    chain = 1
    while x != 1:
        if x in chain_list:
            chain += chain_list[x]
            return chain
        elif x%2 == 0:
            x //= 2
        else:
            x = 3*x + 1
        chain += 1
    return chain

longest_chain = 0
longest_chain_num = 0
num = 1
chain_list = {}
while num < 10**6:
    chain = Collatz(num)
    if chain > longest_chain:
        longest_chain = chain
        longest_chain_num = num
    chain_list[num] = chain
    num += 1
print(longest_chain,longest_chain_num)