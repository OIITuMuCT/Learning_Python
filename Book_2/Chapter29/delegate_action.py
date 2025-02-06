class Super:
    def delegate(self):
        self.action()
    def action(self):
        assert False, 'action must be defined!' # Если вызвана эта версия
    def action(self):
        raise NotImplementedError('action must be defined!!') # Вызывается этот метод первым

class Sub(Super):
    def action(self):
        print('spam')


# x = Super()
# x.delegate()
x = Sub()
x.delegate()