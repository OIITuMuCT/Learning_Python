def F(num):
    return int(num)
test = int(input())

if test > 0:
    def func():
        print(f'num {test} is positive')
else:
    def func():
        print(f'num {test} is negative')


othername = func  # Присваивание объекта функции
othername()  # Снова вызывает func

func.attr = 'spam'
print(func.attr)
print(func.__dict__)
func.name = ''
print(func.__dict__)
func.name = print(f'{func.__name__} test positive or negative number')
func.name
print(func.__dict__)
