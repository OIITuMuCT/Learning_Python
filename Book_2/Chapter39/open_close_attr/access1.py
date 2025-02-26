""" файл access1.py (Python 3.X + 2.X) 
Защита для атрибутов, извлекаемых из экземпляров класса.
Пример приведен в коде самотестирования в конце файла.
Декоратор такой же, как Doubler = Private('data', 'size')(Doubler).
Private возвращает onDecorator, onDecorator возвращает onInstance,
а в каждом экземпляре onInstance внедрен экземпляр Doubler.
"""
traceMe = False
def trace(*args):
    if traceMe:
        print('['+ ' '.join(map(str, args)) + ']')


def Private(*privates):                     # privates в объемлющей области видимости

    def onDecorator(aClass):                # aClass в объемлющей области видимости

        class onInstance:                   # wrapped в атрибуте экземпляра
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)
            def __getattr__(self, attr):
                trace('get:', attr)         # Предполагается, что остальные внутри wrapped
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)
            def __setattr__(self, attr, value): # операции доступа извне
                trace('set: ', attr, value)     # остальные выполняют нормально
                if attr =='wrapped':            # Разрешить доступ к собственным атрибутам
                    self.__dict__[attr] = value     # Избежать зацикливания
                elif attr in privates:
                    raise TypeError('private attributes change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value) # Атрибуты внутреннего объекта 
                    
        return onInstance                               # Либо использовать __dict__
    return onDecorator

if __name__ == '__main__':
    traceMe = True
    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start
        def size(self):
            return len(self.data)
        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))
X = Doubler('X is', [1, 2, 3])
Y = Doubler('Y is', [-10, -20, -30])

# Весь следующий код выполняется успешно
print(X.label)
X.display(); X.double(); X.display()

print(Y.label)
Y.display(); Y.double()
Y.label = 'Spam'
Y.display()
# Весь следующий код должным образом терпит неудачу
""" 
print(X.size())
print(X.data)
X.data = [1,1,1]
X.size = lambda S: 0
print(Y.data)
print(Y.size)
"""
