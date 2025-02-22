calls = 0
def tracer(func, *args):
    global calls
    calls += 1
    print('Call %s to %s' % (calls, func.__name__))
    func(*args)

def spam(a,b, c):
    print(a+b+c)


if __name__ == '__main__':
    spam(1, 2, 3)           # Нормальный вызов без отслеживания: случайный?
    tracer(spam, 1, 2, 3)   # Специальный вызов с отслеживанием без декораторов
