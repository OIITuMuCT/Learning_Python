class rec: pass

def uppername(obj):
    return obj.name.upper()

if __name__ == '__main__':
    rec.name = 'Bob'
    rec.age = 40
    rec.fruit = 'banana'
    rec.method =  uppername
    print(rec.name)
    print(rec.age)
    y = rec()
    x = rec()
    x.name = 'Sergun'
    print(x.name)
    print(y.name)
    print(list(rec.__dict__.values()))
    print(list(name for name in rec.__dict__ if not name.endswith("__")))
    print(list(x.__dict__.keys()))
    print(x.__class__) # Связь экземпляра класса
    print(isinstance(x, rec))
    print(uppername(x))
    print(y.method())
