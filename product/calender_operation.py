import calendar
import datetime
print(calendar.calendar(2018,w = 3,l = 2,c = 4))
'''     calendar.calendar(year,w,l,c) is return calendar.
        w=width of character
        l=no of line
        c=space
'''
from calendar import monthrange



print(calendar.isleap(2012))

'''     isleap year is used to check a year is leap year or not 
        return True if leap year then else False
'''
        
print("no of leapyears:",calendar.leapdays(2010,2030))

'''     it is used to get no of leap years between range of year.    '''


print(calendar.firstweekday())

'''     its used to give default day of week start with 0 monday   '''

print(calendar.month(2018,12,w=4,l=1))
'''    its used to get specific month calendar    '''

print("start month day and total days",calendar.monthrange(2018,12))
'''    its used to get day number of month and numbers of days in month    '''


dt = '20/12/2018'
day, month, year = (int(x) for x in dt.split('/'))    
ans = datetime.date(year, month, day)
start_day=calendar.monthrange(year,month)
print(start_day[0])
print(ans.strftime("%A"))
temp=day+(start_day[0])
print(int(temp/7))

'''     it give day name and its number of day in month    '''

