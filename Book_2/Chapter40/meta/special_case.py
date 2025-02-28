# The built-ins special case


class C:                        # Особый случай наследования #2. . .
    attr = 1                    # Для встроенных имен пропускается шаг
    def __str__(self):
        return('class')


I = C()
print(I.__str__(), str(I))      # Оба имени из класса, если нет в экземпляре
I.__str__ = lambda: 'instance'
print(I.__str__(), str(I))      # Явное=>экземпляр, встроенное=>клаcc!
I.attr = 2
print(I.attr)                   # Асимметрично с нормальными или явными именами


class D(type):
    def __str__(self):
        return ('D class')

class C(D):
    pass

print(C.__str__(C), str(C))     # Явное=>суперкласс, встроенное=>метакласс!

class C(D):
    def __str__(self):
        return ('C class')

print(C.__str__(C), str(C))     # Явное=>класс, встроенное=>метакласс!

class C(metaclass=D):
    def __str__(self):
        return (
            'C class'
        )
print(C.__str__(C), str(C)) # Встроенное=>метакласс, определяемый пользователем

class C(metaclass=D):
    pass

print(C.__str__(C), str(C))  # Явное=>object, встроенное=>метакласс
print(C.__str__)
for k in (C, C.__class__, type):
    print([x.__name__ for x in k.__mro__])