class Squares:
    def __init__(self, start , stop):
        self.start = start
        self.stop = stop
    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

if __name__ == '__main__':
    S = Squares(1, 5)
    I = iter(S.gen())
    print(I)
    # next(I)
    # next(I)
    # next(I)
    for i in I:
        print(i, end=' ')
    # print(next(I))