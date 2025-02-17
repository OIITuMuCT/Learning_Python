class Found(Exception): pass

def searcher():
    if ...успех...:
        raise Found()       # Генерировать исключения вместо возвращения флагов
    else:
        return
try:
    searcher()
except Found:               # Исключение, если элемент был найден
    ...успех...
else:                       # иначе элемент не был найден
    ...неудача...