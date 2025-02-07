class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        if attrname == 'name':
            return 'Петя'
        else:
            raise AttributeError(attrname)

if __name__ == '__main__':
    X = Empty()
    print('X.age =>',X.age)
    print('X.name =>', X.name)
    print("X.lastname =>", X.lastname)
