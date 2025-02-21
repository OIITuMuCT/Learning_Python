def decorator(A, B):
    # Сохранение либо использование A, B
    def actualDecorator(F):
        # Сохранение либо использование функций F
        # Возвращение вызываемого объекта: вложенного def, класса с __call__ и т.д.
        return callable
    return actualDecorator 