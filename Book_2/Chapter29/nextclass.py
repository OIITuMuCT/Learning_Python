class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)


x = NextClass()
x.printer('instance call')
print(x.message)