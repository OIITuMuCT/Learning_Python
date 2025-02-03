class Person:
    def __init__(self, name, jobs, age=None): # Класс = данные + логика
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        return (self.name, self.jobs)


if __name__ == '__main__':
    
    rec1 = Person('Bob', ['dev', 'mgr'], 40.5)  #  Вызовы конструктора
    rec2 = Person('Sue', ['dev', 'cto'])
    print(rec1.jobs, rec2.info()) # атрибуты + методы
    
    rec3 = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])   # dict
    rec4 = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
    print(rec3, rec4)
    # rec5 = Rec('Bob', 40.5, ['dev', 'mgr'])  # ??? Именованные кортежи 