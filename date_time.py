import datetime as dt
import calendar as c

date= dt.date.today()
print(date.day ,"/" ,date.month, "/", date.year)
print("October","", date.day,"",date.year)

time=dt.time(10,30,55)
print(time)

yy=2024
mm=10
print(c.month(yy,mm))