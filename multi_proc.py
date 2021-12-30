import os
import time
from multiprocessing import Process

class sProcess(Process):
    def __init__(self,count):
        super().__init__()
        self.count = count

    def run(self):
        num = 0
        for x in range(self.count*10000000):
            num += 1
        print(f"pid： -> {os.getpid()} finished ")


# def task1(n):
#     for x in range(n):
#         print(f"task1 -> {x} ")
#
# def task2(n):
#     for x in range(n):
#         print(f"task2 -> {x} ")
#
# def task3(n):
#     for x in range(n):
#         print(f"task3 -> {x} ")

if __name__ == '__main__':
    p1 = sProcess(3)
    p2 = sProcess(3)
    p3 = sProcess(3)

    # t1 = time.time()
    # task1(30000)
    # task2(30000)
    # task3(30000)
    # t2 = time.time()
    # print(t2 - t1)

    t1 = time.time()
    p1.start()
    p2.start()
    p3.start()
    t2 = time.time()
    print(t2 - t1)

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.time()
    print(end - start)


