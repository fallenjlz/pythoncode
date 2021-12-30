"""
创建列表的五种方法计时比较：空列表append、列表解析、map函数调用、生成器表达式、生成器函数
"""

import time
import trace
import sys

def time_choose():
    return time.time() if sys.platform != 'windows' else time.count()

def timer(func,*args,_reps=10000,**kargs):
    # trace(func,*args,**kargs)
    init_time = time_choose()
    for x in range(_reps):
        ret = func(*args,**kargs)
    end_time = time_choose()
    eclapsed = end_time - init_time
    return (eclapsed, ret)

def best_timer(func,*args,_reps=50,**kargs):
    best = 2 ** 32
    init_time = time_choose()
    if _reps < best:
        best = _reps
    for x in range(best):
        ret = func(*args, **kargs)
    end_time = time_choose()
    eclapsed = end_time - init_time
    return (eclapsed, ret)

repls = 10000

def for_loop():
    lis = []
    for i in range(repls):
        lis.append(i)
    return lis

def list_comp():
    return [i for i in range(repls)]

def map_call():
    return list(map(abs,range(repls)))

def gen_expr():
    return list(i for i in range(repls))

def gen_func():
    def gen():
        for i in range(repls):
            yield i
    return list(gen())

if __name__ == "__main__":
    for tim in [timer,best_timer]:
        print("="*40)
        for tester in [for_loop,list_comp,map_call,gen_expr,gen_func]:
            used_time,ret = tim(tester)
            print("-"*30)
            print("{0} {1}used_time: {2} list_start:{3} list_end{4}".format(tim.__name__,tester.__name__, used_time, ret[0], ret[-1]))
