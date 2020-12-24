import os, sys, time

def createDaemon(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    #产生子进程，而后父进程退出
    try:
        pid = os.fork()
        if pid > 0 : sys.exit(0)
    except Exception as error:
        print(f"fork error : {error}")
        sys.exit(1)
    os.chdir("/")#修改子进程工作目录
    os.setsid()#创建新的会话，子进程成为会话的首进程
    os.umask(0)#修改工作目录的umask
    #创建孙子进程，而后子进程退出
    try:
        pid = os.fork()
        if pid > 0:
            print(f"Daemon PID {pid}")
            sys.exit(0)
    except Exception as error:
        print(f"fork error : {error}")
        sys.exit(1)

    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'w')

    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())


def ping():
    try:
        os.system('ping www.baidu.com')
    except OSError as err:
        print(f"os error: {err}")

def run():
    while True:
        sys.stdout.write(f"start time---------:{time.ctime()}\n")
        sys.stdout.flush()
        time.sleep(3)
        sys.stdout.write("end of time--------:%s\n"%time.ctime())
        sys.stdout.flush()

if __name__=='__main__':
    createDaemon('/dev/null', f'{os.path.dirname(__file__)}/log.log', '/dev/null')
    run()