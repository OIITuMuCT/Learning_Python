# Традиционная форма вызова методов суперкласса: переносимая универсальная
class C:
    def act(self):
        print('spam')
class D(C):
    def act(self):
        C.act(self)
        print('eggs')

if __name__ == '__main__':
    X = D()
    X.act()