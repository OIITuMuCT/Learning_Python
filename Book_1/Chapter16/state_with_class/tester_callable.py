class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):          # Перехватывает прямые обращения к экземпляру
        print(label, self.state)        # Таким образом, .nested() не требуется
        self.state += 1

H = tester(99)
H('juice')      # Вызывает __call__
H('pancakes')
