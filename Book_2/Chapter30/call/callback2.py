class Callback:
    def __init__(self, color):
        self.color = color
    def changeColor(self):
        print('turn', self.color)


if __name__ == '__main__':
    cb1 = Callback('blue')
    cb2 = Callback('yellow')
    
    # B1 = Button(command=cb1.changeColor)
    obj= cb1.changeColor
    obj()