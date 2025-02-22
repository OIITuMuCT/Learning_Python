# State with nonlocal: 3.X only
# Состояние с помощью оператора nonlocal: только Python 3.X
def tester(start):
    state = start   # Каждый вызов получает собственное значение state
    def nested(label):
        nonlocal state  # Запоминает state из объемлющей области видимости
        print(label, state)
        state += 1  # Нелокальную переменную разрешено изменять
    return nested

F = tester(0)
F("spam")   # Переменная state видима только внутри замыкания

print(F.state)  # AttributeError: ’function' object has no attribute 'state'
