import pickle
obj = SomeClass()
file = open(filename, 'wb')      # Создать внешний файл
pickle.dump(object, file)       # Сохранить объект в файле

import pickle
file = open(filename, 'rb')
obj = pickle.load(file)   # Извлечь объект в более позднее время