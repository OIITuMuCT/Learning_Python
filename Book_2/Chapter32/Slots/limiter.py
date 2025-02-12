class limiter(object):
    __slots__ = ['age', 'name', 'job']


if __name__ == '__main__':
    x = limiter()
    x.age = 40
    print(x.age)
    x.name = "Bob"
    print(x.name)