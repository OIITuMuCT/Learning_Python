class C:
    shared = []
    def __init__(self):
        self.perobj = []

if __name__ == '__main__':
    x = C()
    y = C()
    print(y.shared, y.perobj)
    x.shared.append('Spam')
    x.perobj.append('spam')
    print(x.shared, x.perobj)
    print(y.shared, y.perobj)
    print(C.shared)
