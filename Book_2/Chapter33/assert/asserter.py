def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2


if __name__ == '__main__':
    f(1)