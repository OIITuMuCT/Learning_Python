class Failure(Exception):
    pass
def searcher():
    if 'успех':
        return 'найденный элемент'
    else:
        raise Failure()
try:
    item = searcher()
except Failure:
    print('Элемент не найден')
else:
    'использовать элемент'