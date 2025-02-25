class BuiltinsMixin:
    class ProxyDesc(object):
        def __init__(self, attrname):
            self.attrname = attrname
        def __get__(self, instance, owner):
            return getattr(instance._wrapped, self.attrname)    # Предполагается
                                                                # _wrapped
builtins = ['add', 'str', 'getitem', 'call']
for attr in builtins:
    exec('__%s__ = ProxyDesc("__%s__")' % (attr, attr))

# loop equivalent code
# __add__ = ProxyDesc("__add__")
# __str__ = ProxyDesc("__str__")
# ...etc... (и так далее)
