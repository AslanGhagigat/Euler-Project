def d(n):
    div_sum = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            div_sum += i
            if n//i < n:
                div_sum += n//i
    return div_sum


def amicable_pair(a):
    b = d(a)
    if b != a and d(b) == a:
        return True


n = 10000
sum_all_amicable = 0
for i in range(1, n):
    if amicable_pair(i):
        sum_all_amicable += i

print(sum_all_amicable)
