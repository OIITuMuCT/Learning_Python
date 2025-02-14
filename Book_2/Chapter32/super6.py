class A:
    def method(self): print('A.method'); super().method()

class B(A):
    def method(self): print('B.method'); super().method()

class C:
    def method(self): print('C.method')

class D(B, C):
    def method(self): print('D.method'); super().method()

if __name__ == '__main__':
    X = D()
    X.method()