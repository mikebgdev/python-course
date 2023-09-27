from datetime import datetime


def print_date(date):
    print(date.hour)
    print(date.day)
    print(date.year)
    print(date.month)
    print(date.date())
    print(date.timestamp())


now = datetime.now()
year_2023 = datetime(2023, 1, 1, 12, 45, 30)

print_date(now)
print_date(year_2023)

from datetime import time

current_time = time(21, 6, 45)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2023, 9, 27)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.today())

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)


