class Indexer:
    data = [5,6,7,8,9]
    def __getitem__(self, index):
        print('getitem: , index')
        return self.data[index]
    


if __name__ == '__main__':
    X = Indexer()
    print(X[0])
    print(X[2:4])