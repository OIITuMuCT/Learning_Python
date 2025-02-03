class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)



if __name__ == '__main__':
    first = FirstClass()
    first.setdata("Potato")
    first.display()
    tomato = FirstClass()
    tomato.setdata('tomato')
    tomato.display()
    tomato.data = "Cucumber"
    tomato.display()
    second = SecondClass()
    second.display()
