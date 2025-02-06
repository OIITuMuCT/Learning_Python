X = 11                                  # Global name in module

def g1():                               # Ссылка на глобальное имя в модуле(11)
    print('g1() = ', X)

def g2():                               
    global X
    print('g2() , Gloabal X = ', X)
    X = 22                              # Изменение глобального имени в модуле
    print('g2() = ', X)

def h1():
    X = 33                              # Локальное имя в функции
    def nested():
        print('h1(), nested() = ', X)         # Ссылка на локальное имя в объемлющей области видимости (33)
    return nested

def h2():
    X = 33                             # Локальное имя в функции
    print('локальное имя в функции h2() = ', X)
    def nested():
        nonlocal X                      # Оператор в Python 3.X
        print('nonlocal X = ', X)
        # X = 44                      # Изменение локального имени в объемлющей области видимости
        print('h2(), nested() = ', X)
    return nested

g1()
g2()
h1()
h1()()
h2()
h2()()
