import multiprocessing
import os
from time import sleep

def worker():
    """worker function"""
    print(f"worker pid={os.getpid()}")
    sleep(20)
    print('Worker')
    return

if __name__ == '__main__':
    jobs = []
    print(f"main pid={os.getpid()}")
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()