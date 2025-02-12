class Spam:
    numInstances = 0            # Отслеживание переданного класса
    def __init__(self):
        Spam.numInstances +=1
    def printNumInstances(cls):
        print("Number of instances: %s %s" % (cls.numInstances, cls))
    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):             # Переопределение метода класса
        print('Extra stuff...', cls)        # С вызовом первоначального метода
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam):          # Наследование метода класса
    pass


def main():
    x = Sub()
    y = Spam()
    x.printNumInstances()               # Вызов из экземпляра подкласса
    Sub.printNumInstances()             # Вызов из самого подкласса
    y.printNumInstances()               # Вызов из экземпляра суперкласса
    z = Other()                         # Вызов из экземпляра более низкого подкласса
    z.printNumInstances()

if __name__ == '__main__':
    main()