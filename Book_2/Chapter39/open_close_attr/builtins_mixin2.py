class BuiltinsMixin:
    """ Перенаправляющий класс """
    def reroute(self, attr, *args, **kwargs):
        return self.__class__.__getattr__(self, attr)(*args, **kwargs)
    def __add__(self, other):
        return self.reroute('__add__', other)
    def __str__(self):
        return self.reroute('__str__')
    def __getitem__(self, index):
        return self.reroute('__getitem__', index)
    def __call__(self, *args, **kwargs):
        return self.reroute('__call__', *args, **kwargs)
    # plus any others needed
