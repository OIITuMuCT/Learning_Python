
class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr + ' not allowed')

if __name__ == '__main__':
    X = Accesscontrol()
    X.age = 40
    print(X.age)
    X.name = 'Bob'
    print(X.name)