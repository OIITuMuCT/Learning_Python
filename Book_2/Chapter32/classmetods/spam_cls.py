class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print('Number of instances: %s' % cls.numInstances)
    printNumInstances = classmethod(printNumInstances)

def main():
    a, b = Spam(), Spam()
    a.printNumInstances()
    Spam.printNumInstances()


if __name__ == '__main__':
    main()