class tester:                           # Альтернатива на основе класса (см, часть VI)

    def __init__(self, start):          # При создании объектов состояние
        self.state = start              # явно сохраняется в новом объекте

    def nested(self, label):        
        print(label, self.state)        # Явная ссылка на состояние
        self.state += 1                 # Изменения также разрешены


F = tester(0)       # Создание экземпляра, вызов __init__ 
F.nested('spam')    # F передается аргументу self
F.nested('ham')
G = tester(42)      # Каждый экземпляр получает новую копию состояния
G.nested("toast")   # Изменение одного не влияет на остальные
G.nested('bacon')
F.nested("eggs")    # Состояние F осталось прежним
print(F.state)      # Доступ к состоянию возможен извне класса
print(G.state)
