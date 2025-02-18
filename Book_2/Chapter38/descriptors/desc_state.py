class DescState:    # Использование состояния дескриптора , (object) in Python 2.X
    """
    Состояние дескриптора применяется для управления либо данными, используемыми
    при внутренней работе дескриптора, либо данными, которые охватывают
    все экземпляры. Оно может варьироваться в зависимости от места появления
    атрибута (часто в зависимости от клиентского класса)
    """
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):  # При извлечении атрибута
        print('DescStane get')
        return self.value * 10

    def __set__(self, instance, value):  # При присваивании атрибута
        print('DescState set')
        self.value = value


# Клиентский класс
class CalsAttrs:
    X = DescState(2)        # Атрибут класса дескриптора
    Y = 3                   # Атрибут класса
    def __init__(self):
        self.Z = 4          # Атрибут экземпляра


obj = CalsAttrs()
print(obj.X, obj.Y, obj.Z)
print(DescState.__doc__)
