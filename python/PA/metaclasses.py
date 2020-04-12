class Meta(type):
    def __new__(*args):
        print('new {}'.format(args))
        return type.__new__(*args)
    def __init__(*args):
        print('init {}'.format(args))
        return type.__init__(*args)
    def __call__(*args):
        print('call {}'.format(args))
        #return type.__call__(*args[:-1], args[-1] * 2)

class Class(metaclass=Meta):
    def __init__(self, a):
        self.a = a
        print('constructor')
    def m(self, a):
        print(a)
        return a * 2

if __name__ == '__main__':
    a = Class(2)
    print(a.a)
    a.m(12)
