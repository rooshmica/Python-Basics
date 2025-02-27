
import datetime

# get a date object representing today
this_date = datetime.date.today()
print("Today is", this_date.strftime("%A %d %B %Y"))

# create a date object for New Year's Day 2021
new_years_day = datetime.date(2021,1,1)
print("New Year's Day 2021 will be on a", this_date.strftime("%A"))

# calculate the difference between today and New year's Day:
delta = new_years_day - this_date
print("Number of days until New Year's Day 2021:", delta.days)

