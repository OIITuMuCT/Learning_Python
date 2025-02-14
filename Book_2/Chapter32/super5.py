class A:
    def __init__(self):
        print("A.__init__")


class B(A):
    def __init__(self):
        print("B.__init__")
        A.__init__(self)


class C(A):
    def __init__(self):
        print("C.__init__")
        A.__init__(self)

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)


if __name__ == "__main__":
    x = B()
    x = C()
    x = D()
    print(B.__mro__)
