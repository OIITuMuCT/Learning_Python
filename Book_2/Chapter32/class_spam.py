class Spam:
    # Переменная счетчик
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances():
        print('Number of instances created: %s' % Spam.numInstances)


def main():
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.printNumInstances()
    # Spam().printNumInstances()
if __name__== '__main__':
    main()

