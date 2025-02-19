class DescBoth:
    def __init__(self, data):
        self.data = data
    def __get__(self, instance, owner):
        return '%s, %s' % (self.data , instance.data)
    def __set__(self, instance, value):
        instance.data = value

class Client:
    def __init__(self, data):
        self.data = data
    managed = DescBoth('spam')

if __name__ == '__main__':
    I = Client('eggs')
    print(I.managed)
    I.managed = "SPAM"
    print(I.managed)
    print(I.__dict__)
    print([x for x in dir(I) if not x.startswith('__') ])
    print(getattr(I, 'data'))
    print(getattr(I, 'managed'))
    for attr in (x for x in dir(I) if not x.startswith('__')):
        print('%s => %s' % (attr, getattr(I, attr)))
    print()