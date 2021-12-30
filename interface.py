class Super:
    def method(self):
        print('super method')
    def delegate(self):
        self.action()

class Overwrite(Super):
    def method(self):
        print('sub class method')

class Delegates(Super):
    def method(self):
        print('.'*30)
        Super.method(self)
        print('.'*30)

class Provider(Super):
    def action(self):
        print('action is here')

if __name__ == '__main__':
    o1 = Overwrite()
    d1 = Delegates()
    p1 = Provider()
    o1.method()
    d1.method()
    p1.delegate()
