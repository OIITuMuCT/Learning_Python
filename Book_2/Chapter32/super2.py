class C:
    def act(self):
        print('spam')
    # def fact(self):
    #     print('ham')
class D(C):
    def act(self):
        super().act()       # Обобщенная ссылка на суперкласс, без self
        print('eggs')
        # super().fact()
class E(C):
    def method(self):
        proxy = super()
        print(proxy)
        proxy.act()

if __name__ == "__main__":
    X = D()
    X.act()
    E().method()
