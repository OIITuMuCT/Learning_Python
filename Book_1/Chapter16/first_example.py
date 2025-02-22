def times(x, y):
    return x * y

print(times(2, 4))
x = times(3.14, 4)
print(x)
print(times('Ni', 4))
times.pi = 3.14
print(times(times.pi, 4))

