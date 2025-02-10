""" Объекты несвязанных методов(класс): без self.
Доступ к функциональному атрибуту класса путем уточнения с помощью 
класса возвращает объект несвязанного метода. Чтобы вызвать метод,
потребуется в первом аргументе явно указать объект экземпляра.
"""

class Selfless:
    """ Unbound methods """
    def __init__(self, data):
        self.data = data
    def selfless(arg1 , arg2):   
        """ простая функция """
        return arg1 + arg2
    def normal(self, arg1, arg2):
        """ при вызове ожидается экземпляр """
        return self.data + arg1 + arg2

if __name__ =="__main__":
    X = Selfless(2)
    print(X.normal(3, 4))                   # Экземпляр передается self автоматически: 2 + (3+4) 
    print(Selfless.normal(X, 3, 4))         # Метод ожидает self: передать в ручную
    print(Selfless.selfless(3, 4))          # Без передачи экземпляра: работает только в Python 3.X