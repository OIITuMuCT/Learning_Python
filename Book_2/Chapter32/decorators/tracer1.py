class tracer:
    def __init__(self, func):       # запоминает исходный начальный счетчик
        self.calls = 0
        self.func = func

    def __call__(self, *args):      # При последующих вызовах: добавляет логику, 
                                    # запускает оригинал
        self.calls +=1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)
    
@tracer
def spam(a, b, c):
    return a + b + c
print(spam(1, 2, 3))
print(spam('a', 'b', 'c'))
    