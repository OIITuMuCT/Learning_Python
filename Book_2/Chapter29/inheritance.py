class Super:
    def method(self):
        print('in Super.method')

class Sub(Super):
    def method(self):                   # Переопределить метод
        print('starting Sub.method')    # Добавить здесь нужные действия
        Super.method(self)              # Запустить стандартное действие
        print('ending Sub.method')
        
if __name__ == '__main__':
    x = Super() 
    x.method()
    x = Sub()
    x.method()