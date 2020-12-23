import time, os

now = time.strftime('%X', time.localtime())
print(now)

print(f'{os.path.dirname(__file__)}/log.log')