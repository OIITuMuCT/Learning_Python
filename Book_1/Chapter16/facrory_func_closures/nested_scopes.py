def func():
    x = 4
    action = lambda n: x**n     # x запоминается из объемлющего def
    return action

x = func()
print(x(2))                     # Выводит 16, 4 *★ 2
