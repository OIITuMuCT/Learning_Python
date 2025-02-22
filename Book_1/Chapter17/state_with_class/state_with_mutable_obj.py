def tester(start):
    def nested(label):
        print(label, state[0])  # Использует в своих интересах изменение
                                # на месте изменяемого объекта
        state[0] += 1           # Добавочный синтаксис, глубинная магия?
    state = [start]
    return nested

F = tester(0)
F('spam')
F('eggs')
G = tester(42)
G('spam')
G('hammer')
