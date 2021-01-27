import multiprocessing
import os
import sys
from time import sleep

def worker():
    """worker function"""
    print(f"worker pid={os.getpid()}")
    sleep(20)
    print('Worker')
    sys.exit(5)

if __name__ == '__main__':
    jobs = []
    print(f"main pid={os.getpid()}")
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
    for pid in jobs:
        print(pid)

    for pid in jobs:
        pid.join()
    print(f"main pid={os.getpid()}")
    for pid in jobs:
        print(pid)
