def tester(start):
    global state        # Вынести в модуль, чтобы можно было изменять
    state = start       # global делает возможными изменения
                        # в области видимости модуля
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F("spam")       # Каждый вызов инкрементирует разделяемое глобальное состояние
F('eggs')
G = tester(42)
G('spam')
G('eggs')
G('spam')
F('eggs')
