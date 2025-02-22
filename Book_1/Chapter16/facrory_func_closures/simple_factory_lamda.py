# A simple function factory
def maker(N):
    return lambda X: X**N   # Функции lambda тоже сохраняют состояние

h = maker(3)
print(h(4))                 # Снова 4 ** 3
