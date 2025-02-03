# запись на основе кортежа
rec = ('Bob', 40.5, ['dev', 'mgr']) 
print(rec[0], rec.__class__)
# запись на основе словаря.
rec = {}  
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['jobs'] = ['dev', 'mgr']

print(rec['name'], rec.__class__)
# Запись на основе класса.
class rec: pass
rec.name = 'Bob'
rec.age = 40.5
rec.jobs = ['dev', 'mgr']

print(rec.name, rec.__class__)

# запись на основе экземпляров
pers1 = rec()
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rec()
pers2.name = "Sue"
pers2.jobs = ["dev", "cto"]
pers2.age = 25
print(pers1.name, pers2.name)
