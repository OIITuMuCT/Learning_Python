import shelve
object = SomeClass()
dbase = shelve.open(filename)
dbase['key'] = object           # Сохранить под ключом

import shelve
dbase = shelve.open(filename)
object = dbase["key"]           # Извлечь объект в более позднее время
