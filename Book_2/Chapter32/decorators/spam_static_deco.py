class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    
    @staticmethod
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)
            # количество созданный экземпляров
    
def main():
    a, b, c = Spam(), Spam(), Spam()
    Spam.printNumInstances()
    a.printNumInstances()


if __name__ == '__main__':
    main()