def func(a, b, c, e=True, f=None):      # Аргументы: три обязательных,
                                        # два со стандартными значениями
    x = 1                               # Плюс еще две локальные переменные
    y = 2

code = func.__code__
print(code.co_nlocals)                         # Количество аргументов общее
print(code.co_varnames)                        # Все имена локальных переменных
print(code.co_varnames[: code.co_argcount])    # <== Первые N имен локальных переменных
# являются ожидаемыми аргументами

def catcher(*args, **kwargs): print('%s, %s' % (args, kwargs))

print("выводится на экран: args - как кортеж, а kwargs - как словарь")
catcher(1, 2, c=3, d=4, e=5)

# import sys                        # Для обратной совместимости
# tuple(sys.version_info)           # [0] - старший номер версии
# code = func.__code__ if sys.version_info[0] == 3 else func.code_code
