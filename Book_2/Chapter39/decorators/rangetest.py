""" 
Файл rangetest.py: декоратор функций, который выполняет проверку вхождения 
в диапазон для аргументов, переданных любой функции или методу.

Аргументы указывают декоратору по ключам. В фактическом вызове аргументы 
могут передаваться по позициям или по ключам, а аргументы со стандартными
значениями разрешено опускать. Примеры сценариев использования ищите в файле
rangetest_test.py
"""
trace = True

def rangetest(**argchecks): # Проверять вхождение в диапазон для аргументов 
                            # обоих видов и аргументов со стандартными значениями
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            def onCall(*args, **kwargs):
                # Все элементы args соответствуют первым N
                # ожидаемых аргументов по позициям
                # Остальные должны быть в kwargs или быть опущены
                # из-за наличия стандартных значений
                expected = list(allargs)
                positionals = expected[:len(args)]
                for (argname, (low, high)) in argchecks.items():
                    # Для всех аругментов, подлежащих проверке
                    if argname in kwargs:
                        # Был передан по имени
                        if kwargs[argname] < low or kwargs[argname] > high:
                            # Аргумент не находится в диапазоне 
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        # Был передан по позиции
                        position = positionals.index(argname)
                        if args[position] < low or args[position] > high:
                            # Аргумент не находится в диапазоне
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    else:
                    # Предполагается, что не был передан: имеет стандартное значение
                        if trace:
                            # Аргумент имеет стандартное значение
                            print('Argument "{0}" defaulted'.format(argname))
                return func(*args, **kwargs) # Нормально: выполнить исходный вызов
            return onCall
    return onDecorator