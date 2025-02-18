class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        "name property docs"
        print('fetch...')
        return self._name
    @name.setter
    def name(self, name):
        print('change...')
        self._name = value