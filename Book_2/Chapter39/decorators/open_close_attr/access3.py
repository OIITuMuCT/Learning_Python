# Вставка методов: остальной код в access2 остается прежним
def accessControl(failIf):
    def onDecorator(aClass):
        def getattributes(self, attr):
            trace('get: ', attr)
            if failIf(attr):
                raise TypeError('private attribute fetch: ' + attr)
            else:
                return object.__getattribute__(self, attr)
        def setattributes(self, attr, value):
            trace('set: ' + attr)
            if failIf(attr):
                raise TypeError('private attribute change: ' + attr)
            else:
                return object.__setattr__(self, attr, value)
        aClass.__getattribute__ = getattributes
        aClass.__setattr__ = setattributes      # Вставка методов доступа
        return aClass                           # Возвращение исходного класса
    return onDecorator
