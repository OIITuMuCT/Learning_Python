class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):             # name = property(name)
        "name property docs"    # Документация по свойству name
        print('fetch...')       # Извлечение...
        return self._name
    @name.setter
    def name(self, value):      # name = name.setter(name)
        print('change...')      # Изменение...
        self._name = value
    @name.deleter               # name = name.deleter(name)
    def name(self):
        print('remove...')      # удаление...
        del self._name

if __name__ == '__main__':
    bob = Person('Bob Smith')       # экземпляр bob имеет управляемый атрибут
    print(bob.name)                 # Запускается метод getter свойства name (name1)
    bob.name = 'Robert Smith'       # Запускается метод setter свойства name (name2) 
    print(bob.name)

    del bob.name                    # Запускается метод deleter свойства name (name3) 

    print('-'*20)
    sue = Person('Sue Jones')       # Экземпляр sue тоже наследует свойство
    print(sue.name)
    print(Person.name.__doc__)      # Или help(Person.name)
    # print(help(Person.name))
    print(list(sue.__dict__.keys()))
