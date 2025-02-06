class Indexer:
    def __getitem__(self, index):
        return index ** 2

if __name__ == '__main__':
    X = Indexer()
    print(X[2])
    for i in range(1,11):
        print(X[i], end=' ')