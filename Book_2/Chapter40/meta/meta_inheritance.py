class M1(type):
    attr1 = 1  # Дерево наследования метаклассов


class M2(M1): # Получает имена__ bases__ ,__class__, __mro__
    attr2 = 2  


class C1:       # Дерево наследования суперклассов
    attr3 = 3  


class C2(C1, metaclass=M2):     # Получает имена__ bases__ ,__class__, __mro__
    attr4 = 4  


if __name__ == '__main__':
    I = C2()    # I получает __class__ f но не остальные имена
    print(I.attr3) # Экземпляр наследует имена из дерева суперклассов
    print(I.attr4)
    print(
        C2.attr1, C2.attr2, C2.attr3, C2.attr4
    )  # Класс получает имена из обоих деревьев !
    print(M2.attr1, M2.attr2)  # Метакласс тоже наследует имена!
    print(I.__class__)
    print(C2.__bases__)
    print(C2.__class__)
    print(M2.__bases__)
    print(I.__class__.attr1)
    # print(I.attr1) # exc AttributeError
    print(M2.__class__)
    print([x.__name__ for x in C2.__mro__])
    print([x.__name__ for x in M2.__mro__])