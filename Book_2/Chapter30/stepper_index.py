class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


X = StepperIndex()
X.data = 'Spam'
print(X[1])
for item in X:
    print(item, end=' ')
print()
print((list(X), tuple(X), ''.join(X)))