class Super:
    def method(self): ...                   # Действительный прикладной метод

class Tool:
    def __method(self): ...                 # Превращается в _Tool__method
    def other(self): self.__method()        # использовать внутренний метод

class Sub1(Tool, Super):
    def actions(self): self.method()        # Выполняется Super.method, как и ожидалось
class Sub2(Tool):
    def __init__(self): self.method = 99  # Не нарушает работу Tool.__method