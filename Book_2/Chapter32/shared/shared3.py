class C:
    shared = []                 # общий список
    def __init__(self):
        self.perobj = []

def main():
    x = C()
    y = C()
    # добавили элемент в список 
    x.shared.append('spam')
    x.perobj.append('spam')
    print(x.shared, x.perobj)   # Выводит на экран ['spam'] и ['spam']

    y.shared.append('eggs')
    y.perobj.append('ham')
    print(y.shared, y.perobj)   # Выводит на экран ['spam', 'eggs'] и  ['ham']

    print(x.shared, x.perobj)  # Выводит на экран ['spam', 'eggs'] и ['spam'] первый фокус)))
    x.shared = ['eggs']
    print(x.shared, x.perobj)  # Выводит на экран ['eggs'] и ['spam']
    y.shared.append('ham')
    print(y.shared)             #!  Что будет здесь????

if __name__ == '__main__':
    main()
