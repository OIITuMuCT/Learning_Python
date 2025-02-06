from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    @abstractmethod
    def method(self):
        pass

# В версии Python 2.6 и 2.7 взамен мы используем атрибут класса:
# class Super:
#     __metaclass__ = ABCMeta
#     @abstractmethod
#     def method(self):
#         pass
