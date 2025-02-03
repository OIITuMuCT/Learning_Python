import example1
class SecondClass(example1.FirstClass):
    def display(self):
        print(f'Current value = {self.data}')

if __name__ == '__main__':
    second = SecondClass()
    num = SecondClass()
    num.setdata(45)
    second.setdata(42)
    second.display()
    num.display()
    print(second.data)
    print(num.data)