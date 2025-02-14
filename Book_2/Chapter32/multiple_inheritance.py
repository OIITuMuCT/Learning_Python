class ListTree:
    def __str__(self): ...
    def other(self): ...

class Super:
    def __str__(self): ...
    def other(self): ...


class Sub(ListTree, Super):     # Получить метод str из класса ListTree, указав его первым
    other = Super.other         # Но явно выбрать версию other из класса Super
    def __init__(self):
        ...


if __name__ == '__main__':
    x = Sub()                   # Поиск при наследовании производится в Sub
                                # и затем в ListTree/Super
    print(x)
