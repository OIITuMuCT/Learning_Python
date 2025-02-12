def count(aClass):
    aClass.numInstances = 0
    return aClass               # Возвращает сам класс, а не оболочку

@count
class Spam: ...                 # То же самое, что и Spam = count(Spam)

@count
class Sub(Spam): ...            # numInstances = 0 здесь не требуется

@count
class Other(Spam): ...

@count
def spam(): pass                # Подобно spam = count(spam)

@count
class Other: pass               # Подобно Other = count(Other)

spam.numInstances       # Оба устанавливаются в 0
Other.numInstances