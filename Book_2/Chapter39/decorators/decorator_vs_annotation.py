def rangetest(**argchecks):
    def onDecorator(func):
        def onCall(*args, **kwargs):
            print(argchecks)
            for check in argchecks:
                pass  # Добавить сюда код проверки допустимости
            return func(*args, **kwargs)
        return onCall
    return onDecorator


@rangetest(a=(1, 5), c=(0.0, 1.0))
def func(a, b, c):  # func = rangetest (. . .) (func)
    print(a + b + c)


func(1, 2, c=3)  # Запускается onCall, argchecks в области видимости


# Использование аннотаций функций (только Python З.Х)
def rangetest(func):
    def onCall(*args, **kwargs):
        argchecks = func.__annotations__
        print(argchecks)
        for check in argchecks:
            pass
        return func(*args, **kwargs)
    return onCall

@rangetest
def func(a:(1, 5), b, c:(0.0, 1.0)): # func = rangetest(func)
    print(a + b + c)

func(1, 2, c=3)