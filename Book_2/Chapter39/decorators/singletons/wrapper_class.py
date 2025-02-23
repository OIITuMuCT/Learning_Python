class Wrapper:
    def __init__(self, object):
        self.wrapped = object                       # Сохранение объекта

    def __getattr__(self, attrname):            
        print("Trace: ", attrname)                  # Отслеживание извлечения
        return getattr(self.wrapped, attrname)      # Делегирование извлечения

if __name__=='__main__':
    x = Wrapper([1, 3, 4])
    x.append(5)
    print(x.wrapped)
    
    x = Wrapper({'a': 1, 'b': 2})
    print(list(x.keys()))
    