class Adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        return self.data + other
    def __str__(self):
        return f'[Value: {self.data}]'

if __name__ == '__main__':
    x = Adder(5)
    x = x + 2
    # x = 2 + x  # TypeError: unsupported operand type(s) for +: 'int' and 'Adder'

    print(x)
