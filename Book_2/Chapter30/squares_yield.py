class Squares:
    def __init__(self, start , stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

if __name__ == '__main__':
    for i in Squares(1, 7):
        print(i, end=' ')
    S = Squares(1, 5)
    I = iter(S)
    print(next(I))
    