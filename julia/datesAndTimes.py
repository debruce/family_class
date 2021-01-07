import datetime
import calendar
import dateutil
from datetime import date

def convert(string): 
    con = list(string.split(" ")) 
    return con

x = input("What do you want to know?: ")

if x == "weekday":
    y = date.today()
    print("The day is", calendar.day_name[y.weekday()])
elif x == "time":
    print("The time is", datetime.time)
elif x == "date":
    print("The date is", datetime.date)
elif x == "date distance":
    f_date = input("Enter a date: ")
    l_date = input("Enter a second date: ")
    a = datetime.datetime.strptime(f_date, "%Y-%m-%d")
    b = datetime.datetime.strptime(l_date, "%Y-%m-%d")
    c = abs(b - a)
    print("The number of days between those dates is ", c.days)
else: 
    print("Try 'weekday', 'time', 'date', or 'date distance'.")

