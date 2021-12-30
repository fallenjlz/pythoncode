import sys
class STREAM:
    def __init__(self,reader,writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while 1:
            data = self.reader.readline()
            if not data:
                break
            else:
                data = self.conver(data)
                self.writer.write(data)
    def __str__(self):
        return '%s' % (self.writer.readlines())

class UPPERCASE(STREAM):
    def conver(self,args):
        return args.upper()


if __name__ == '__main__':
    import sys
    UPPERCASE(open('test'),open('testw','w')).process()
    print(UPPERCASE(open('test'),open('testw','w')))