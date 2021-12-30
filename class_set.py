#!/usr/local/bin/python3.9
# class Set:
#     def __init__(self,value=[]):
#         self.data = []
#         self.concat(value)
#
#     def intersect(self,other):
#         res = []
#         for x in self.data:
#             if x in other:
#                 res.append(x)
#         return Set(res)
#
#     def union(self,other):
#         res = self.data[:]
#         for x in other:
#             if x not in res:
#                 res.append(x)
#         return Set(res)
#
#     def concat(self,value):
#         for x in value:
#             if x not in self.data:
#                 self.data.append(x)
#
#     def __len__(self): return len(self.data)
#     def __getitem__(self, item): return self.data[item]
#     def __and__(self, other): return self.intersect(other)
#     def __or__(self,other): return self.union(other)
#     def __repr__(self): return repr(self.data)
class Set(list):
    def __init__(self,value=[]):
        list.__init__([])
        self.concat(value)

    def intersect(self,other):
        res = [x for x in self if x in other]
        return Set(res)

    def union(self,other):
        res = self[:]
        for x in other:
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self,value):
        for x in value:
            if x not in self:
                self.append(x)

    # def __len__(self): return len(self)
    # def __getitem__(self, item): return self[item]
    def __and__(self, other): return self.intersect(other)
    def __or__(self,other): return self.union(other)
    def __repr__(self): return list.__repr__(self)

if __name__ == '__main__':
    s1 = Set([2,3,4,6,7])
    s2 = Set([3,4,5,9,8,7,10])
    print(s1 & s2)
    print(s1 | s2)
    print(s1)
    print(s2)
    for x in s1:
        print(x)
    print(s2[3])
