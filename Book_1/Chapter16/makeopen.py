import builtins

def makeopen(id):
    original = builtins.open
    def custom(*args, **kwargs):
        print('Custom open call %r:' % id, args, kwargs)
        return original(**args, **kwargs)
    builtins.open = custom