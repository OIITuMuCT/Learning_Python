class Indexer:
    data = [5,6,7,8,9]
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing',  index)
        else:
            print('slicing', index.start, index.stop, index.step)



if __name__ == '__main__':
    X = Indexer()
    print(X[99])
    # print(X[0])
    # print(X[2:4])