from multiprocessing import Pool
import asyncio
import time


async def test(time):
    print("start")
    await asyncio.sleep(time)  # 调用协程内的时间间隔
    print("end")


async def main(num):
    start_time = time.time()
    tasks = [asyncio.create_task(test(3)) for proxy in range(num)]  # 注册任务列表
    print(len(tasks))
    print("协程结束时间：", time.time() - start_time)


def run(num):
    asyncio.run(main(num))  # 使用协程调用方法


if __name__ == "__main__":
    """
        start_time = time.time()
    p = Pool()
    # 启动多个进程，在每个进程内运行协程任务
    for i in range(4):
        # apply(): 阻塞主进程, 并且一个一个按顺序地执行子进程, 等到全部子进程都执行完毕后 ,继续执行 apply()后面主进程的代码
        # apply_async() 非阻塞异步的, 他不会等待子进程执行完毕, 主进程会继续执行, 他会根据系统调度来进行进程切换
        p.apply_async(run, args=(10,))
    p.close()
    p.join()
    print("进程结束时间：", time.time() - start_time)

    """
    run(10)
