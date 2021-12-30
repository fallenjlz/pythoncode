import sys
class General(Exception):
    pass

class sub1(General):
    def __init__(self,item1, item2):
        super(sub1, self).__init__()
        self.item1 = item1
        self.item2 = item2

class sub2(General):
    pass


class A(Exception):
    pass

class B(A):
    def __init__(self,t1, t2):
        super(B, self).__init__()
        self.t1 = t1
        self.t2 = t2

class C(B):
    pass

if __name__ == '__main__':
    try:
        # raise sub1('test','good')
        raise sub2('sub2','throw')
    except sub2 as s :
        print(s.args)

    try:
        raise C('exp','c')
    except B as y:
        print(y.t1, y.t2)
    except A as x:
        print(x.args)
    finally:
        print("just done!!!")