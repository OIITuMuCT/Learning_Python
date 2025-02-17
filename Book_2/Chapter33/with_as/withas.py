"""
Протокол управления контекстами 
1. Выражение вычисляется, давая в результате объект диспетчера контекста, 
который обязан иметь методы __enter__ и __exit__.
2. Вызывая метод __enter__ диспетчера контекста. Возвращаемое им значение
присваивается переменной в конструкции as при ее наличии либо попросту 
отбрасывается.
3. Выполняется код во вложенном блоке with.
4. Если в блоке with возникает исключение, тогда вызывается метод 
__exit__(type, value, traceback) с передачей ему деталей исключения. Это
те же самые значения, которые возвращает функция sys.exc_info, описанная
в руководствах по Python. Если метод __exit__ возвращает False, тогда 
исключение генерируется повторно; иначе оно заканчивается. Обычно исключение
должно быть сгенерировано заново, чтобы оно распространилось за пределы 
оператора with.
5. Если в блоке with исключение не возникло, то метод __exit__ все равно 
вызывается, но для всех его аргументов type, value и traceback передаются
None.
"""
class TraceBlock:
    def message(self, arg):
        print('running ' + arg)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))
            return False

if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test 1')
        print('reached')
    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')