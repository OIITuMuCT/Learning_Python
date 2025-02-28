class D:
    def __get__(self, instance, owner):
        print('__get__')
    def __set__(self, instance, value):
        print('__set__')

class C:
    d = D()
    c = D()

if __name__ == '__main__':
    I = C()
    I.d = 4
    I.c = 3
    