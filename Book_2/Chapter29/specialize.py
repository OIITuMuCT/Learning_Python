"""Методика связывания классов """
class Super:
    """ 
    Определяет функцию method и метод delegate, 
    который ожидает наличие в подклассе метода action 
    """
    def method(self):
        print('is Super.method')                # Стандартное поведение
    def delegate(self):
        self.action()                           # Ожидает определение метода

class Inheritor(Super):                         # Буквальное наследование метода
    """
    Не предоставляет никаких новых имен, поэтому получает все, 
    что определено в Super.
    """
    pass

class Replacer(Super):                          # Полное замещение метода
    """ 
    Переопределяет method из Super посредством собственной версии.
    """
    def method(self):
        print('in Replace.method')              # в Replacer.method

class Extender(Super):                          # Расширение поведение метода
    """ 
    Настраивает method из Super, переопределяя и обеспечивая 
    выполнение стандартного поведения
    """
    def method(self):
        print('starting Extender.method')       # начало Extender.method
        Super.method(self)
        print('ending Extender.method')         # конец Extender.method

class Provider(Super):                          # в Provider.method
    """ 
    Реализует метод action, ожидаемый методом delegate из Super.
    """
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
    print(Super.__name__, Super.__doc__)
    print(Inheritor.__name__, Inheritor.__doc__)
    