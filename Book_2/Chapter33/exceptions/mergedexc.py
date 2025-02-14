# файл mergedexc.py (Python 3.X + 2.X)
sep = '-' * 45 + '\n'
# Исключение генерируется и перехватывается
print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

# Исключения не генерируются
print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

# Исключение не генерируется, конструкцией else
print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

# Исключение генерируется, но не перехватывается
print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')