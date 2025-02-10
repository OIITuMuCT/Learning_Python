class Callback:
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print('turn', self.color)

if __name__=='__main__':
    cb1 = Callback('blue')      # запомнить blue
    cb2 = Callback("green")     # запомнить green

    # B1 = Button(command=cb1)  # зарегистрировать обработчики
    # B2 = Button(command=cb2)
    # События
    cb1()  # выводит turn blue
    cb2()  # выводит turn green
