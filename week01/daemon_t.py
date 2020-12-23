import os,sys,time

def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as err:
        sys.stderr.write(f"_Fork #1 fail:{err}\n")
        sys.exit(1)

    os.chdir('/')
    os.umask(0)
    os.setsid()

    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as err:
        sys.stderr.write(f"_Fork #2 fail:{err}\n")
        sys.exit(1)

    sys.stdout.flush()
    sys.stderr.flush()

    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'w')

    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

def test():
    sys.stdout.write(f"Daemon starded with pid {os.getpid()}") # os.getpid()：获取当前进程的pid
    while True:
        now = time.strftime('%X', time.localtime())
        sys.stdout.write(f'{now}\n') # 输出当前的时间标识，即当前的的时分秒
        sys.stdout.flush() # 刷新当前缓冲区
        time.sleep(1)

if __name__ == "__main__":
    daemonize('/dev/null', f'{os.path.dirname(__file__)}/log.log', '/dev/null')
    test()