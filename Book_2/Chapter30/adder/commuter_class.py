class Commuter1:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

if __name__ == '__main__':
    x = Commuter1(88)
    y = Commuter1(99)
    x = x + 1
    print(x)
    y = 1 + y
    print(y)
    
    print(x + y)