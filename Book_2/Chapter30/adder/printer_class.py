class Printer:
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

if __name__ == '__main__':
    objs = [Printer(2), Printer(3)]
    for x in objs:
        print(x)
    print(objs)
    print(objs.__str__)
