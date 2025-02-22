def tracer(func):   # Состояние чрез объемлющую область
    # видимости и глобальную переменную
    calls = 0       # Вместо атрибутов класса или глобальных переменных
    def wrapper(*args, **kwargs):   # calls - для каждой функции,
                                    # не глобальная переменная
        nonlocal calls
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper


@tracer
def spam(a, b, c):  # To же, что и spam = tracer(spam)
    print(a + b + c)


@tracer
def eggs(x, y):  # To же, что и eggs = tracer(eggs)
    print(x**y)


if __name__ == "__main__":
    spam(1, 3, 4)               # На самом деле вызывается wrapper, присвоенный spam
    spam(a=4, b=5, c=6)         # wrapper вызывает spam
    eggs(2, 16)                 # На самом деле вызывается wrapper, присвоенный eggs
    eggs(4, y=4)                # Глобальная переменная calls не является
                                # отдельной для каждого случая декорирования!
