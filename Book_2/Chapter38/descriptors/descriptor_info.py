class Descriptor:
    "docstring goes here"                       # Строка документации
    def __get__(self, instance, owner): ...     # Возвращает значение атрибута
    def __set__(self, instance , value): ...    # Ничего не возвращает None
    def __delete__(self, instance): ...         # Ничего не возвращает None

