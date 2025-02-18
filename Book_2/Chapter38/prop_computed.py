class PropSquare:
    def __init__(self, start):
        self.value = start
    def getX(self):                 # При извлечении атрибута
        return self.value ** 2

    def setX(self, value):          # При присваивании атрибута
        self.value = value

    X = property(getX, setX)        # Удаления и документации не предусмотрено


if __name__ == '__main__':
    P = PropSquare(3)
    Q = PropSquare(32)
    print(P.X)
    P.X = 4
    print(P.X)
    print(Q.X)