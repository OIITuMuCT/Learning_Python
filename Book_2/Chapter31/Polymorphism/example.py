class C:
    def __init__(self, *args):
        self.val =  args
    def meth(self, *args):
        if len(args) == 1:
            print('Len(args) == 1')
        elif type(args[0]) == int:
            print('args[0] == int')
        else:
            print('else', args)

if __name__ == '__main__':
    X = C([1, 2, 3], (1, 2, 3))
    print(X.val)
    X.meth('len', 'dir')
