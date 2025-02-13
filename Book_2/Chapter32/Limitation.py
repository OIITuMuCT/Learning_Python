# Limitation: Operator overloading

class C:

    def __getitem__(self, ix):      # Метод перегрузки операции индексирования
        print('C index')


class D(C):

    def __getitem__(self, ix):      # Переопределение с целью расширения
        print('D index')
        C.__getitem__(self, ix)     # Традиционная форма вызова работает
        super().__getitem__(ix)     # Прямые вызовы по имени тоже работают
        # super()[ix]               # Но операции - нет! (__ getattribute__ )


if __name__ == '__main__':
    X = C()
    X[99]
    X = D()
    X[99]
