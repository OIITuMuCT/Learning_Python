class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other

if __name__=='__main__':
    X = C()
    print(X > 'ham')
    print(X < 'ham')
    