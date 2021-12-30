from functools import reduce

def f1(*args):
    return reduce(lambda a,b: a*b,(x for x in args))