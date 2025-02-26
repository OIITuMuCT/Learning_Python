class InstState:  # Использование состояния экземпляра, (object) в Python 2.Х
    """
    Состояние экземпляра хранит информацию, связанную и возможно созданную
    клиентским классом. Оно может варьироваться в зависимости от экземпляра
    клиентского класса (т.е. в зависимости от объекта приложения).
    """
    def __get__(
        self, instance, owner):  # Предполагается, что установлен клиентским классом
        print('InstState get')
        return instance._X * 10

    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value


# Клиентский класс
class CalcAttrs:
    X = InstState()             # Атрибут класса дескриптора
    Y = 3                       # Атрибут класса
    def __init__(self): 
        self._X = 2             # Атрибут экземпляра
        self.Z = 4              # Атрибут экземпляра


obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)      # X вычисляется, остальные нет
obj.X = 5                       # Присваивание X перехватывается
CalcAttrs.Y = 6                 # Y повторно присваивается в классе
obj.Z = 7                       # Z присваивается в экземпляре
print(obj.X, obj.Y, obj.Z)
obj2 = CalcAttrs()              # Но X теперь отличается подобно Z!
print(obj2.X, obj2.Y, obj2.Z)
