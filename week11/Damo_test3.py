import random
from multiprocessing import Pool
import os,time

def run():
    time.sleep(random.random() * 3)
    print(os.getpid())
    with open('test.txt', 'a') as f:
        f.write(time.time())

if __name__ == '__main__':
    p = Pool(4)
    for i in range(10):
        p.apply_async(func=run)
    p.close()
    p.join()
    p.terminate()