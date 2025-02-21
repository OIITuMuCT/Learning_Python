# Statement of expressions my_func('spam', 'eggs', meat=ham, *rest)

# def
def printer(message):
    print('Hello' + message)
printer(' Greg House!')
# return
def adder(a, b=1, *c):
    return a + b + c[0]
print(adder(1, 2, 3, 4))

# global
x = 'old'
def changer():
    global x
    x = 'new'
    return x
print(changer())

# nonlocal
def outer():
    x = 'old'
    def changer():
        nonlocal x
        x = 'new2'
        return x
    return changer()
print(outer())

# yield
def squares(x):
    for i in range(x):
        yield i ** 2

# lambda
funcs = [lambda x: x**2, lambda x: x**3]
print(funcs)