class Callee:
    def __call__(self, *args, **kwargs):
        print('Called', args, kwargs)

if __name__=='__main__':
    C = Callee()
    x = C(1, 2, 3)
    y = C(1, 2, 3, x = 4, y=5)
