# Основы
def __getattr__(self, name):        # При извлечении неопределенных атрибутов [obj.name]
def __getattribute__(self, name):   # При извлечении всех атрибутов [obj.name]
def __setattr__(self, name, value): # При присваивании всех атрибутов [obj.name = value]
def __delattr__(self, name):        # При удалении всех атрибутов [del obj.name]
