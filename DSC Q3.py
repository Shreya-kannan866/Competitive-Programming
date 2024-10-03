import calendar
import datetime
day_of_year=int(input("Enter the day of the year:"))
year=int(input("Enter the year:"))
is_leap=calendar.isleap(year)
date=datetime.datetime(year,1,1)+datetime.timedelta(days=day_of_year-1)
print(date.strftime('"%d %B, '),year,'"')
    
   
