def tracer(func):
    def oncall(*args):
        oncall.calls +=1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer
    def spam(self, a, b, c): return a + b + c


if __name__ == '__main__':
    x = C()
    print(x.spam(1, 2, 3))
    print(x.spam('a', 'b', 'c'))