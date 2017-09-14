class FooParent(object):
    def __init__(self):
        print 'Parent'
    def test(self):
        print 'foo parent'

class FooChild(FooParent):
    def bar(self):
        self.test()
        FooParent.test(self)
        super(FooChild, self).test()


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar()
