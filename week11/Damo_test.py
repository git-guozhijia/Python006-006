from multiprocessing import Pool
import os, time, random


def run_task(name):
    print(f'Task {name} (pid = {os.getpid()}) (ppid = {os.getppid()}) is running...')
    time.sleep(random.random() * 3)
    print(f"Task {name} end.")


if __name__ == "__main__":
    print(f'Current process {os.getpid()}.')
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print("Waiting for all subprocesses done...")
    p.close()
    p.join()
    print('All subprocesses done.')
    p.terminate()
