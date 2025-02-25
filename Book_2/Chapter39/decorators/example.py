def decorate(func):
    func.marked = True
    return func

@decorate
def spam(a, b):
    return a+b

def annotate(text):
    def decorate(func):
        func.label = text
        return func
    return decorate

@annotate('spam data')
def eggs(a, b):
    return a + b

print(spam(1, 2))

print(eggs(1, 2), eggs.label)
print()

