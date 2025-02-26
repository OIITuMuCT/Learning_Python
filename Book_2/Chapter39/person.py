class Person:

    def giveRaise(self, percent):  # Проверка посредством встраиваемого кода
        if percent < 0.0 > 1.0:
            raise TypeError('percent invalid')
        self.pay = int(self.pay * (1 + percent))

class Person:
    def giveRaise(self, percent): # Проверка посредством утверждений
        assert percent >= 0.0 and percent <= 1.0, 'percent invalid'
        self.pay = int(self.pay * (1 + percent))

class Person:
    @rangetest(perscnt=(0.0, 1.0))
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))