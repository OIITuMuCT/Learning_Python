class Spam:
    numInstances = 0
    def count(cls):                 # Счетчики экземпляров по классам
        cls.numInstances += 1       # cls - самый нижний класс над экземпляром
    def __init__(self):
        self.count()                # передает self.__class__ методу count
    count = classmethod(count)

class Sub(Spam):
    numInstances = 0
    def __init__(self):             # Переопределяет __init__
        Spam.__init__(self)

class Other(Spam):                  # Наследует __init__
    numInstances = 0


def main():
    x = Spam()
    y1, y2 = Sub(), Sub()
    z1, z2, z3 = Other(), Other(), Other()
    l = x.numInstances, y1.numInstances, z1.numInstances
    for m in l:
        print(m, end=' ')
    L = Spam.numInstances, Sub.numInstances, Other.numInstances
    print(L)


if __name__ == '__main__':
    main()