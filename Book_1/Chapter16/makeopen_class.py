class makeopen:
    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self
    def __call__(self, *args, **kwargs):
        print('Custom open call %r:' % self.id, args, kwargs)
        return self.original(*args, **kwargs)
    