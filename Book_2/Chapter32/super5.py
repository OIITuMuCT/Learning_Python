class A:
    def __init__(self):
        print("A.__init__")


class B(A):
    def __init__(self):
        print("B(A).__init__")
        A.__init__(self)


class C(A):
    def __init__(self):
        print("C(A).__init__")
        A.__init__(self)


if __name__ == "__main__":
    x = B()
    x = C()
