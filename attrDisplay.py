class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__.keys()):
            attr = '%s=%s'%(key,getattr(self,key))
            attrs.append(attr)
        return ','.join(attrs)
    def __str__(self):
        return '%s: %s'%(self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':

    class Test(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = Test.count
            self.attr2 = Test.count + 1
            Test.count += 2
    class subTest(Test):
        pass

    t1 = Test()
    t1.gatherAttrs()
    t2 = subTest()
    t2.gatherAttrs()
    print(t1)
    print(t2)