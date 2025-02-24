instances = {}
def getInstance(aClass, **args, **kwargs):
    if aClass not in instances:
        instances[aClass] = aClass(*args, **kwargs)
    return instances[aClass]
bob = getInstance(Person, 'Bob', 40, 10)