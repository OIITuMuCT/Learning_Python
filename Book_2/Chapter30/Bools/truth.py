class Truth:
    def __bool__(self):
        return True
class Lies:
    def __bool__(self):
        return False
    def __len__(self): return 0



if __name__ == '__main__':
    X = Truth()
    if X:
        print('yes!')
    Y = Lies()
    if Y:
        print('yes!')
    else:
        print('no!')