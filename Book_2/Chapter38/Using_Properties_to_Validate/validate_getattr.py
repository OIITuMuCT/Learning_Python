class CardHolder:
    acctlen = 8                                             # Данные класса
    retireage = 59.5
    def __init__(self, acct, name, age, addr):      
        self.acct = acct                                    # Данные экземпляра
        self.name = name                                    # Тоже запускают__ setattr__
        self.age = age                                      # Имя _acct не корректируется:
        # проверяется name
        self.addr = addr                                    # Имя addr не является управляемым
        # remain не имеет данных
    def __getattr__(self, name):
        if name == "acct":                                  # При извлечении неопределенных атрибутов
            return self._acct[:-3] + "***"                  # name, age, addr определены
        elif name == 'remain':
            return self.retireage - self.age                # He запускает__ getattr__
        else:
            raise ArithmeticError(name)
    def __setattr__(self, name, value):
        if name == "name":                                  # При операциях присваивания всех атрибутов
            value = value.lower().replace(" ", "_")         # addr хранится напрямую
        elif name == "age":                                 # acct корректируется в _acct
            if value < 0 or value > 150:
                return ValueError("invalid age")            # недопустимый возраст
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError("invalid acct number")      # недопустимый номер счета
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value         # Избегание зацикливания
        # (или через object)
