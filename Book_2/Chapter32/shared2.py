class C:
    shared = []
    def __init__(self):
        self.perobj = []
class A:
    def __init__(self):
        self.name = []
    def __str__(self):
        return 'Class A obj'
    



if __name__ == '__main__':
    x = C()
    y = C()
    x.shared.append('spam')
    x.perobj.append('spam')
    print(x.shared, x.perobj)
    y.shared.append('eggs')
    print(y.shared, y.perobj)
    print(x.shared, x.perobj)
    x.shared = 'eggs'
    print(y.shared)
    print(x.shared.__class__)
    print(x)
    z = A()
    y.shared.append(z)
    print(y.shared)
    print(C.shared[2])
    print(z.name)