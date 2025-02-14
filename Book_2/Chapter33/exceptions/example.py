class AlreadyCotOne(Exception): pass     # Исключение определяемое пользователем

def grail():
    raise AlreadyCotOne()               # Генерирует экземпляр

try:
    grail()
except AlreadyCotOne:                   # Перехват по имени класса
    print('got exception')              # Получено исключение