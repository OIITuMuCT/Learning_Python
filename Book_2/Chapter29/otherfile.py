import manynames
X = 66
print('otherfile X =', X)                   # 66: здесь глобальное имя
print('manynames.X = ', manynames.X)        # 11: после импортирования глобльные имена становятся атрибутами

manynames.f()                               # 11: имя Х из модуля manynames, не то, которое находится здесь!

manynames.g()                               # 22: локальное имя из функции в другом файле

print('manynames.C.X = ', manynames.C.X)    # 33: атрибут класса в другом модуле
I = manynames.C()                           
print("I.X = ", I.X)                        # 33: здесь все еще имя из класса
I.m()                                       
print('I.X (after I.m())', I.X)             # а теперь имя из экземпляра!
