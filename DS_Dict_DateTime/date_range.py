
import datetime

dates_list = []

# open the files
with open("amazon_english_correct_dates.csv", "r", encoding="utf-8") as infile:
    # read the headers from the first line of the infile and discard
    infile.readline()
    
    # read in each line of the input file
    for line in infile:
        # split the line into component variables
        year, state, month, fires, date_string = line.strip().split(",")        
        
        # convert the date string to a date object and add it to the list
        dates_list.append(datetime.date.fromisoformat(date_string))
        
# Results
print("Number of dates:", len(dates_list))
# the date objects can be processed by max the and min functions
earliest = min(dates_list)
print("Earlist date:", earliest) 
latest = max(dates_list)
print("Latest date:", latest)

# determine the range of dates, the difference between the latest and earliest
delta = latest - earliest
print("Number of days between the earliest and latest dates:", delta.days)

