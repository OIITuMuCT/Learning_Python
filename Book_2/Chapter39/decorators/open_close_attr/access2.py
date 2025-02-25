""" 
Файл access2.py (Python 3.X + 2.X)
Декораторы классов с объявлениями атрибутов Private и Public.
Управляют внешним доступом к атрибутам, хранящимся в экземпляре или 
унаследованным из его классов.
Private объявляет имена атрибутов, которые нельзя извлекать или присваивать
им значения за пределами декорируемого класса, а Public объявляет все имена,
к которым можно применять упомянутые действия.

Предостережение: в Python 3.X это работает только явно именованных 
атрибутов: в классах
нового стиля методы перезагрузки операций __X__, неявно запускаемых для
встроенных операций,
не вызывают ни __getattr__, ни __getattribute__. Чтобы перехватывать и 
делегировать выполнение
встроенных операций, необходимо добавить здесь методы __Х__.
"""
traceMe = False
def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')
def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, **args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)
            
            def __getattr__(self, attr):
                trace('get: ' attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set: ', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator


def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))

