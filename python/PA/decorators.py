from traceback import print_stack

def memoization(f):
    f.cache = {}
    def f1(*args):
        if args in f.cache:
            return f.cache[args]
        else:
            f.cache[args] = f(*args)
            return f.cache[args]
    return f1

def logging(f, file='log.txt'):
    def f1(*args):
        out = open(file, 'a')
        out.write(f.__name__)
        for a in args:
            out.write(' ' + str(a))
        out.write('\n')
        out.close()
        return f(*args)
    return f1

def stack_tracer(f):
    def f1(*args):
        print_stack()
        return f(*args)
    return f1

@memoization
@stack_tracer
def double(x):
    print('Computing double of {}.'.format(x))
    return x*2

@memoization
@logging
def pow(x, y):
    print('Computing {} to the power of {}.'.format(x, y))
    return x**y

@logging
def empty(*args, **kwargs):
    print('Executing empty with args {} and kwargs {}'.format(args, kwargs))

class Test:
    @memoization
    @stack_tracer
    @logging
    def m(self, a, b, c):
        print('Computing {} + {} + {}.'.format(a, b, c))
        return a + b + c

if __name__ == '__main__':
    print(double(3))
    print(double(3))
    print(double(4))
    print(double(5))
    print(double(4))
    print(double(3))

    print(pow(2, 3))
    print(pow(2, 3))
    print(pow(2, 5))
    print(pow(3, 2))
    print(pow(2, 5))
    print(pow(2, 3))

    empty(2, 5)

    t = Test()
    print(t.m(1, 2, 3))
    print(t.m(1, 2, 3))
    print(t.m(1, 2, 3))
