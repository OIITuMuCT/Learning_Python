class Callback:
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print('turn', self.color)


def callback(color):
    def oncall():
        print("turn", color)

    return oncall


if __name__=='__main__':
    cb1 = Callback('blue')      # запомнить blue
    cb2 = Callback("green")     # запомнить green
    cb3 = callback("yellow")
    cb4 = (lambda color=' red': 'turn' + color)
    # B1 = Button(command=cb1)  # зарегистрировать обработчики
    # B2 = Button(command=cb2)
    # События
    cb1()  # выводит turn blue
    cb2()  # выводит turn green
    cb3() 
    print(cb4())