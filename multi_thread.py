from threading import Thread
from time import time


class overThread(Thread):
    def __init__(self,target,args):
        Thread.__init__(self)
        self.target = target
        self.args = args

    def run(self):
        return self.target(*self.args)


def task(*args):
    num = 0
    for x in args:
        num += x


if __name__ == '__main__':
    t1 = overThread(task,list(range(1000000)))
    t2 = overThread(task,list(range(2000000)))
    start = time()
    t1.start();t1.join()
    t2.start();t2.join()
    end = time()
    print(end - start)

