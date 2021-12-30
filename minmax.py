# def lessthan(*args):
#     min = args[0]
#     for a in args[1:]:
#         if a < min:
#             min = a
#     return min
#
# def morethan(*args):
#     max = args[0]
#     for a in args[1:]:
#         if a > max:
#             max = a
#     return max
#
# def minmax(func,*args):
#     return func(*args)
#
#


def minmax(func,*args):
    ret = args[0]
    for a in args[1:]:
        if func(a,ret):
            ret = a
        # ret = ret if func(ret, a) else a
    return ret

def lessthan(x,y): return x < y
def morethan(x,y): return x > y
print(minmax(lessthan,*[1,2,3,4,5]))
print(minmax(morethan,*[1,2,3,4,5]))
