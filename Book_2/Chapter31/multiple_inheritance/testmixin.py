#!python
""" 
Обобщенный инструмент тестирования подмешиваемых классов вывода списков:
он похож на средством транзитнивной перезагрузки модулей из главы 25 первого 
тома, но ему передается объект класса (не функции), а в testByNames
добавлена загрузка модуля и класса по строковым именам в соответствии с 
паттерном проектирования "Фабрика".
"""
import importlib
def tester(listerclass, sept=False):
    class Super:
        def __init__(self):
            self.data1 = 'spam'
        def ham(self):
            pass
    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42
        def spam(self):
            pass
    
    instance = Sub()
    print(instance)
    
    if sept: print('-' * 80)

def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    
    listerclass = getattr(modobject, classname)
    
    tester(listerclass, sept)

if __name__ == '__main__':
    testByNames('listinstance', 'ListInstance', True)

    testByNames('listinherited', 'ListInherited', True)
    testByNames('listtree', 'ListTree', False)