from datetime import datetime,timedelta,timezone,date

import time,pytz
''' Get Current month, current date, current week day, current year, and add hours, minutes, days, 
    month and years in it. '''
from _datetime import date
from time import localtime
    
print(time.localtime(time.time()))


''' Convert time to string and string to time '''
  
print("String to time : ",datetime.strptime('Dec 18 2018  7:20 Tue', '%b %d %Y %H:%M %a'))

now=datetime.now()
print("Time to String: ",now.strftime("%A %d %b %Y"))
 
''' Get Current month name from date. '''
 
get_month=datetime.today()
print("Get month name from date: ",get_month.strftime("%B"))

''' Get time in 12-hour clock & 24-hour clock '''

time_24=datetime.now().time()
print("time in 24 hour formate: ",time_24.strftime('%H:%M'))
print("time in 12 hour formate: ",time_24.strftime('%I:%M'))

''' Get Datetime with century number and without century number. ie. 2018 & 18. '''

print("century number",datetime.today().strftime('%Y'))
print("without century number",datetime.today().strftime('%y'))

''' Difference of 2 Date times. '''

date1=datetime.now()
time.sleep(5)
date2=datetime.now()

time_difference=date2-date1
print("Difference of time: ",time_difference)


''' Addition of 2 Date times. '''
def convert_sec(time):
    
    total_second=sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))

    return total_second

time1 = datetime.now().time().strftime('%H:%M:%S')
sec=convert_sec(time1)

time2=datetime.now().time().strftime('%H:%M:%S')
sec2=convert_sec(time2)
sum_sec=(sec+sec2)

print("Addtion of 2 date time: ",str(timedelta(seconds=sum_sec)))#timedelta is convert seconds to time

''' Get local timezone and current  UTC time. and Convert it in local timezone. also convert it in other timezone. '''

local_time=datetime.now(pytz.timezone('Asia/Kolkata'))
print("Locat time: ",local_time.strftime('%Y-%m-%d %H:%M:%S %z'))

utc_dt = datetime.now(timezone.utc)
''' get utc time
    utc_dt:utc date and time
 '''
 
dt = utc_dt.astimezone()
''' get local time
    dt:date time
'''

print(" utc time:",utc_dt,"\n local time:",dt)

''' Combine date and time object with timezone. '''

mytime =datetime.strptime('130','%H%M').time()
mydatetime =datetime.combine(date.today(), mytime)
print("combine date and time: ",mydatetime)


''' Get Day of year from date time. (01,...366) '''

d1 = datetime.strptime("01 Jan 18", "%d %b %y")
d2=((datetime.now() - d1).days)
print("day of year: ",d2)

''' Get Week number of year by both (Sunday as First Day of week & Monday as First Day of week). '''

testdate=datetime(2018,12,19)
week_No=((testdate - datetime(testdate.year,1,1)).days // 7) + 1
print("week no of year: ",week_No)

''' Get Current Date and Print it in various format like DD/MM/YY, YY/MM/DD, MM-DD-YY, DD-MM-YY, YY-DD-MM '''

print("MM-DD-YY",datetime.today().strftime('%m/%d/%Y'))
print(datetime.today().strftime('%m/%d/%y'))
print("YY/MM/DD",datetime.today().strftime('%Y/%m/%d'))
print(datetime.today().strftime('%y/%m/%d'))
print("DD/MM/YY",datetime.today().strftime('%d/%m/%Y'))
print(datetime.today().strftime('%d/%m/%y'))



