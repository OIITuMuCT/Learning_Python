def decorator(C):  # При декорировании @
    class Wrapper:
        def __init__(self, *args):  # При создании экземпляров: новый объект Wrapper
            self.wrapped = C(*args)     # Внедрение экземпляра в экземпляр
    return Wrapper


class Wrapper: ...
def decorator(C):                   # При декорировании @
    def onCall(*args):              # При создании экземпляров: новый объект Wrapper
        return Wrapper(C(*args))    # Внедрение экземпляра в экземпляр
    return onCall
