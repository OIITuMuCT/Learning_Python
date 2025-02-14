class A:
    def other(self): print('A.other')
class Mixin(A):
    def other(self): print('Mixin.other'); super().other()
class B:
    def method(self): print("B.method")


class C(Mixin, B):
    def method(self): print('C.method'); super().other(); super().method()


# class C(B, Mixin):
#     def method(self):
#         print("C.method")
#         super().other()
#         super().method()


if __name__ == '__main__':
    C().method()
    print(C.__mro__)
