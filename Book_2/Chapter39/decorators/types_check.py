def typetest(**argchecks):
    def onDecorator(func):
        ...
        def onCall(*args, **kwargs):
            positionals = list(allargs)[:len(args)]
            for (argname, type) in argchecks.items():
                if argname in kwargs:
                    if not isinstance(kwargs[argname], type):
                        ...
                        raise TypeError(errmsg)
                elif argname in positionals:
                    position = positionals.index(argname)
                    if not isinstance(args[position], type):
                        ...
                        raise TypeError(errmsg)
                    else:
                        # Предположить, что не передавался: стандартное значение
            return func(*args, **kwargs)
        return onCall
    return onDecorator

