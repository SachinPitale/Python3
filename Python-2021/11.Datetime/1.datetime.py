import datetime


print(dir(datetime))
print(dir(datetime.datetime))
print (datetime.datetime.now())
print (datetime.datetime.today())


"""
# getting other timezone time
import pytz
ist=pytz.timezone('Asia/Kolkata')
print (datetime.datetime.now(ist))
"""

print (datetime.datetime.now().year)
print (datetime.datetime.now().month)
print (datetime.datetime.now().day)
print (datetime.datetime.now().date)
print (datetime.datetime.now().day)
print (datetime.datetime.now().hour)
print (datetime.datetime.now().minute)
print (datetime.datetime.now().second)

print (datetime.datetime.now().strftime("%y-%m-%d"))