class FormatError(Exception): # Унаследованный конструктор
    pass
def parser():
    raise FormatError(42, 'spam.txt') #! Ключевые аргументы на разрешены!
try:
    parser()
except FormatError as X:
    print('Error at:', X.args[0], X.args[1]) # Не специфично для данного приложения
