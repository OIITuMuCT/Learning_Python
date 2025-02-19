"""Отслеживание извлечения каждого атрибута, 
сделанное другим объектом, который передается
классу оболочки"""
class Wrapper:
    """ Перехват аттрибутов """
    def __init__(self, obj):
        self.wrapped = obj                              # Сохранить объект
        self.name = 'Wrapper'

    def __getattr__(self, attrname):
        print("Trace: " + attrname)                     # Отслеживать извлечение
        return getattr(self.wrapped, attrname)          # Делегировать извлечение


if __name__ == '__main__':
    X = Wrapper([1, 2, 3])
    X.append(4)                                         # Выводится Trace: append
    print(X.wrapped)                                    # Выводится [1, 2, 3, 4]
