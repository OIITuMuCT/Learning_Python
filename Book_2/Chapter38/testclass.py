class Test:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def get_name(self):
        # print(self.name)
        return self.name
    def set_name(self, value):
        self.name = value
    def __str__(self):
        return f'<class Test: name = {self.name}, job = {self.job}'


t = Test('Bob', 'mgr')
print(t)
bob = t.get_name()
t.set_name('John')

print(t.name)
print(bob)
print(type(bob))
print(t)
print(Test.__getattribute__)
t.email = 'bob@mail.com'
print(t.email)

