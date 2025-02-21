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
