class adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        self.data += other

x = adder()
print(x)
