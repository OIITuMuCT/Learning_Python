def generate():
    return Spam()


class Spam:  # Определение на верхнем уровне модуля
    count = 1
    def method(self):
        print(Spam.count)   # Работает: в глобальной области видимости


generate().method()
