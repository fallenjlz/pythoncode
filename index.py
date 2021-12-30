# class Indexer():
#     data = [2,3,4,5,6]
#     def __getitem__(self, item):
#         return self.data[item] ** 2


# class Indexer():
#     def __init__(self,start,stop):
#         self.value = start - 1
#         self.stop = stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value == self.stop:
#             raise StopIteration
#         self.value += 1
#         return self.value ** 2

class Iter():
    def __init__(self,value):
        self.data = value
        self.ix = 0

    def __getitem__(self, item):
        print('attr getitem: ', end= '')
        return self.data[item]

    def __iter__(self):
        print('attr iter: ', end='')
        return self

    def __next__(self):
        print('attr next: ', end = '')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item



    def __contains__(self, item):
        print('attr contains:', end = ' ')
        return item in self.data




if __name__ == '__main__':
    x = Iter(list(range(1,5)))
    print(x[slice(3,5)])
    print(x[1])
    print( 3 in x)
    for i in x:
        print(i, end = ' ')
    l = [n for n in x]
    print(l)
