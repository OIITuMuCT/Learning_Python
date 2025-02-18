""" Управляемые атрибуты """


class Person:
    value = ""

    def getName(self):
        if not valid():
            raise TypeError("cannot fetch name")  #  не удается извлечь имя
        else:
            return self.name.transform()

    def setName(self):
        if not valid(value):
            raise TypeError("cannot change name")
        else:
            self.name = transform(value)


person = Person()
person.getName()
person.setName("value")
