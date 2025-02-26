class BuiltinsMixin:
    def __add__(self, other):
        return self.__class__.__getattr__(self, '__add__')(other)
    def __str__(self):
        return self.__class__.__getattr__(self, '__str__')()
    def __getitem__(self, index):
        return self.__class__.__getattr__(self, '__getitem__')(index)
    def __call__(self, *args, **kwargs):
        return self.__class__.__getattr__(self, '__call__')(*args, **kwargs)
    # Плюс любые другие, которые нужны

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance(BuiltinsMixin):
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)
            def __getattr__(self, attr):...
            def __setattr__(self, attr, value):...
        return onInstance
    return onDecorator

