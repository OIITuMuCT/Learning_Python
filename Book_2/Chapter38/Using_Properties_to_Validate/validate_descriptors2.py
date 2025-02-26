""" 
Файл validate_descriptors2.ру: использование состояния 
для каждого экземпляра клиентского класса 
"""
class CardHolder(object):
    """ Держатель карты """
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name(object):
        """ Дескриптор Name """
        def __get__(self, instance, owner):  # Имена классов: локальные в CardHolder
            return instance.__name

        def __set__(self, instance, value):
            value = value.lower().replace(" ", "_")
            instance.__name = value

    name = Name()  # class.name или скорректированное имя атрибута

    class Age(object):
        """ Дескриптор Age """
        def __get__(self, instance, owner):
            return instance.__age  # Использовать данные дескриптора

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                instance.__age = value

    age = Age()

    class Acct(object):
        """Дескриптор Acct"""
        def __get__(self, instance, owner):
            return instance.__acct[:-3] + "***"

        def __set__(self, instance, value):
            value = value.replace("-", "")
            if len(value) != instance.acctlen:
                raise TypeError("invalid acct number")
            else:
                instance.__acct = value

    acct = Acct()

    class Remain(object):
        """Дескриптор Remain, установка не разрешена"""
        def __get__(self, instance, owner):
            return instance.retireage - instance.age

        def __set__(self, instance, value):
            raise TypeError("cannot set remain")

    remain = Remain()
