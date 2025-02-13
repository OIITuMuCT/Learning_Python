class B:
    def __init__(self): print('B.__init__') # Разъединенные ветви дерева классов

class C:
    def __init__(self): print('C.__init__')

class D(B, C): 
    # pass
    def __init__(self):
        B.__init__(self)
        C.__init__(self)

if __name__ == '__main__':
    x = D()

