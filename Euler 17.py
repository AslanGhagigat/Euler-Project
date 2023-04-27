num_to_digit = {
    0: 0,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7,
    1000: 11}

sum_of_digits = 0
# print(num_to_digit)
# n = 300
# for i in range(n, n+1):
for i in range(1, 1001):
    # print('i', i)
    sum_of_digit = 0

    dah_yek = i % 100
    if dah_yek == 0:
        pass
    elif 0 < dah_yek <= 20:
        sum_of_digit += num_to_digit[dah_yek]
    else:
        yek = dah_yek % 10
        dah = dah_yek - yek
        # yek_digit = num_to_digit[yek]
        # dah_digit = num_to_digit[dah]
        sum_of_digit += (num_to_digit[yek] + num_to_digit[dah])

    # print('dah_yek', sum_of_digit)

    sad = i - dah_yek
    if dah_yek != 0 and sad != 0:
        sum_of_digit += 3

    # print('and', sum_of_digit)

    if sad == 0:
        pass
    elif sad == 1000:
        sum_of_digit += num_to_digit[sad]
    else:
        sad_digit = sad // 100
        sum_of_digit += (num_to_digit[sad_digit] + num_to_digit[100])

    # print('sad', sum_of_digit)

    sum_of_digits += sum_of_digit


print(sum_of_digits)
