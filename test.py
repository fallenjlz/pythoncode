def clo(a,b,c):
    print(a,b,c)

clo(1,2,3)


def myzip(*seqs):
    res = []
    minlen = min( len(s) for s in seqs)
    for i in range(minlen):
        g = (s[i] for s in seqs)
        res.append(tuple(g))
    return res

def myzip(*seqs):
     minlen = min( len(s) for s in seqs)
     return [tuple(s[i] for s in seqs) for i in range(minlen)]


def mymap(func,*seqs):
    for s in zip(*seqs):
        yield func(*s)

def sumtree(L):
    sum = 0
    for x in L:
        if not isinstance(x,list):
            sum += x
         else:
             sum += sumtree(x)
    return sum

def func():
    import __main__
    print(__main__.x)
    x = 88
