class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print('Number of instances: %s ' % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances():
        print('Extra stuff...')
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

class Other(Spam):      # Наследование статического метода
    pass

def main():
    # a, b, c = Spam(), Spam(), Spam()
    Spam.printNumInstances()
    # a.printNumInstances()
    a, b = Sub(), Sub()
    a.printNumInstances()
    Sub.printNumInstances()
    Spam.printNumInstances()
    c = Other()
    c.printNumInstances()
if __name__ == '__main__':
    main()