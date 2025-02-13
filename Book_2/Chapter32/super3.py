# Изменения классов во время выполнения и super

class X:
    def m(self): print('X.m')

class Y:

    def m(self):
        print("Y.m")                        # Сначала унаследовать от X


class C(X):
    def m(self): super().m()                # Здесь нельзя жестко закодировать имя класса
    def m(self): C.__bases__[0].m(self)     # ! Специальный код для особого случая
if __name__ == '__main__':
    i = C()
    i.m()
    C.__bases__ = (Y,)                      #! Изменить суперкласс во время выполнения'.
    i.m
