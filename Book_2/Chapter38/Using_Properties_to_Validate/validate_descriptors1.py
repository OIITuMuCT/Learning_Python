# python validate_tester.py validate_descriptors1 команда для запуска
"""
Вариант 1: проверка достоверности с помощью 
разделяемого состояния экземпляра дескриптора
"""

class CardHolder(object):
    acctlen = 8                 # максимальная длина аккаунта
    retireage = 59.5            # Пенсионный возраст

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name(object):
        """ Дескриптор Name """
        def __get__(self, instance, owner):
            return self.name

        def __set__(self, instance, value):
            value = value.lower().replace(" ", "_")
            self.name = value

    name = Name()

    class Age(object):
        """ Дескриптор Age """
        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError("invalid age")
            else:
                self.age = value

    age = Age()

    class Acct(object):
        """ Дескриптор Acct """
        def __get__(self, instance, owner):
            return self.acct[:-3] + "***"

        def __set__(self, instance, value):
            value = value.replace("-", "")
            if len(value) != instance.acctlen:
                raise TypeError("invalid acct number")
            else:
                self.acct = value

    acct = Acct()

    class Remain(object):
        """ Дескриптор Remain, установка не разрешена """
        def __get__(self, instance, owner):
            return instance.retireage - instance.age

        def __set__(self, instance, value):
            return TypeError("cannot set remain")  # Установка не разрешена

    remain = Remain()
