import calendar
import datetime

def getExpiry(year, month):
    # Get the last day of the month
    last_day = calendar.monthrange(year, month)[1]
    
    # Iterate backwards from the last day of the month
    for day in range(last_day, 0, -1):
        date = datetime.date(year, month, day)
        if date.weekday() == 3:  # Thursday (0=Monday, 1=Tuesday, ..., 6=Sunday)
            return date

# Get the current year
# current_year = datetime.datetime.now().year

# Iterate over each month
# for month in range(1, 13):
#     last_thursday_date = last_thursday(current_year, month)
#     print(f"The last Thursday of {calendar.month_name[month]} {current_year} is on {last_thursday_date}")
