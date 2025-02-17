# raise IndexError        # класс (экземпляр создается неявно)
# raise IndexError()      # Экземпляр (создается явно в операторе)

# exc = IndexError()
# raise exc

# excs = [IndexError, TypeError]
# raise excs[0]

class MyExc(Exception):
    pass
raise MyExc("spam")  # Класс исключения с аргументом конструктора

# try:
#     ...
# except MeExc as X:    # Атрибуты экземпляра f доступные в обработчике
#     print(X.args)
