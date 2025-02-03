class C2:
    def __init__(self):
        self.x = 'x с2'
        self.z = 'z с2'

class C3:
    def __init__(self):
        self.w = 'w'
        self.z = 'z с3'

class C1(C2, C3):
    def __init__(self, who):
        self.name = who
        self.x = 'x'
        self.y = 'y'

if __name__ == '__main__':
    I1 = C1('Bob')
    I2 = C1('Sue')
    print(I1.name)
    I3 = C1('Emma')
    print(I3.z)
