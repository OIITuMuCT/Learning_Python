class Number:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):
        self.val += other
        return self

if __name__ == "__main__":
    x = Number(5)
    x += 1
    x += 1
    print(x.val)
    y = Number([1])
    y += [2]
    y += [3]
    print(y.val)
    z = Number([])
    for i in range(int(input())):
        y +=[i]
    print(z.val)
    print(y.val)
    print(y)
    for i in y:
        print(y[i])