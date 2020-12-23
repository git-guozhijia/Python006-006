import time
import datetime

print(time.time())

print(time.strftime("%Y-%m-%d %X", time.localtime()))
print(time.strftime("%Y-%m-%d %X"))
print(time.strftime("%Y-%m-%d"))
print(time.strftime("%Y-%m"))
print(time.strftime("%Y"))
print(time.strftime("%m"))
print(time.strftime("%X"))

print(time.localtime())
print(time.strptime('2020-12-23 10:34:30', "%Y-%m-%d %X"))

print(datetime.datetime.today())
print(datetime.time())
print(datetime.datetime)