class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)

def main():
    print(list('abc'))
    x = MyList('abc')
    print(x)
    print(x[1])
    print(x[3])
    print('Индесинг: ')
    print(x[2])
    x.append('spam')
    print(x)
    x.reverse()
    print(x)


if __name__ == '__main__':
    main()