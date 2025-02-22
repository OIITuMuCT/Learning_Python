class tracer:
    def __init__(self, func):   # При декорировании @: сохранение исходной функции
        self.calls = 0
        self.func = func
    def __call__(self, *args):  # При последующих вызовах: запуск исходной функции
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)
@tracer
def spam(a,b,c):        # spam = tracer (spam)
    print(a+b+c)        # spam помещается в объект декоратора

if __name__ == '__main__':


    spam(10, 15, 20)
    spam(1, 2, 3)