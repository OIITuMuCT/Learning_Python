class Methods:
    """Использование статических методов и методов класса"""
    def imeth(self, x):
        print([self, x])

    def smeth(x):
        """ staticmethod """
        print([x])

    def cmeth(cls, x):
        """ classmethod """
        print([cls, x])

    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)

if __name__ == '__main__':
    obj = Methods()             # Допускает вызов через экземпляр или класс
    obj.imeth(1)
    Methods.imeth(obj, 2)
    Methods.smeth(3)            # Статический метод: вызов через класс
    obj.smeth(4)                # Статический метод: вызов через экземпляр
    Methods.cmeth(5)            # Метод класса: вызывается через класс
    obj.cmeth(6)                # Метод класса: вызывается через экземпляр
