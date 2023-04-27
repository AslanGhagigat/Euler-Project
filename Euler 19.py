months = {"January": 31,
          "February": 28,
          "March": 31,
          "April": 30,
          "May": 31,
          "June": 30,
          "July": 31,
          "August": 31,
          "September": 30,
          "October": 31,
          "November": 30,
          "December": 31}


def LeapYear(x):
    day = 365
    if x % 400 == 0:
        day = 366
    elif x % 100 == 0:
        day = 365
    elif x % 4 == 0:
        day = 366
    if day == 365:
        return False
    else:
        return True

# def today(days: list):
#     days.append(days[0])
#     days.pop(0)
#     return days


def today_num(n: int):
    n += 1
    if n == 7:
        n = 0
    return n


# days = ['tu', 'we', 'th', 'fr', 'sa', 'su', 'mo']
day = 3
# sunday = 0
sunday_num = 0
for year in range(1901, 2001):
    for month in months:
        for i in range(months[month]):
            # days = today(days)
            day = today_num(day)
        if LeapYear(year) and month == 'February':
            # days = today(days)
            day = today_num(day)
        # if days[0] == 'su':
        #     sunday += 1
        if day == 1:
            sunday_num += 1
print(sunday, sunday_num)


# if you uncomment code you calculate days with days name router
# but now you calculate days with number of days router
