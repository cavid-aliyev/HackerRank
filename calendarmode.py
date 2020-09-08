import calendar

list(calendar.day_name)
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

my_month,my_day,my_year=map(int,input().split())

print((calendar.day_name[calendar.weekday(my_year,my_month,my_day)]).upper())