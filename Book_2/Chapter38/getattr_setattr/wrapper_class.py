class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj
        self.name = 'Wrapper'

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)


if __name__ == '__main__':
    X = Wrapper([1, 2, 3])
    X.append(4)
    print(X.wrapped)
    print(X.__dict__)

