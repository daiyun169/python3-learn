# import time
# import calendar

# local_time = time.localtime()
# print(local_time)
#
# new_time = time.mktime((2018, 10, 16, 15, 44, 34, 0, 0, 0))
#
# f_new_time = time.gmtime(new_time)
#
# print(time.strftime('%Y-%m-%d %H:%M:%S %w %W', f_new_time))
#
# print(time.asctime(local_time))
#
# print(time.timezone/3600)
#
# print(time.gmtime(time.time()))

# print(calendar.isleap(2001))
# print(calendar.leapdays(1988, 2018))

# a = 10
# b = 20
# s = 'a+b'
# print(eval(s))

from datetime import date, time, datetime, timedelta
import time as t

# d1 = date(2018, 3, 13)
# print(d1)
#
# d2 = date.today()
# print(d2)
#
# d3 = date.fromtimestamp(t.time())
# print(d3)
#
# print(d1.isoformat())
# print(d1.isocalendar())
# print(d1.isoweekday())
#
# print(d1.strftime('%Y-%m-%d'))
#
# print(d1.timetuple())
#
# for i in d1.timetuple():
#     print(i)

# t = time(12, 13, 14)
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.strftime('%H:%M:%S'))

dt = datetime(2018, 3, 13, 9, 53, 30)
print(dt)

dt2 = datetime.now()
print(dt2)

dt3 = datetime.utcnow()
print(dt3)

dt4 = datetime.fromtimestamp(t.time())
print(dt4)

print(dt4.date())
print(dt4.time())
print(dt4.timestamp())
print(dt4.strftime('%Y-%m-%d %H:%M:%S'))

dl = datetime.now() - dt
print(dl)
print(type(dl))

delta2 = timedelta(days=2, hours=2, seconds=30)
print(delta2)

d3 = datetime.now() + delta2
print(d3)

print(delta2.days)
print(delta2.seconds)
print(2*3600+30)
print(delta2.total_seconds())

