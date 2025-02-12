class Methods(object):
    def imeth(self, x):
        print([self, x])
    
    @staticmethod
    def smeth(x):
        print([x])
    
    @classmethod
    def cmeth(cls, x):
        print([cls, x])
    
    @property
    def name(self):
        return 'Bob ' + self.__class__.__name__

def main():
    obj = Methods()
    obj.imeth(1)
    obj.smeth(2)
    obj.cmeth(3)
    print(obj.name)


if __name__ == '__main__':
    main()
