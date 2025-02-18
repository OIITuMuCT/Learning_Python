class D:
    def __get__(*args):
        print('get')
    def __set__(*args):
        raise AttributeError('cannot set')


class C:
    a = D()

X = C()
X.a                 # Направляется C.a.__ get__
X.a = 99            # Направляется C.a.__ set__
