class Squares:
    def __init__(self, start, stop=0, step=1):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        for value in range(self.start, self.stop, self.step):
            yield value ** 2

for i in Squares(0, 15, 3):
    print(i, end=' ')

S = Squares(1, 15, 3)
I = iter(S)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
# print(next(I))
# print(next(I))
# print(next(I))
