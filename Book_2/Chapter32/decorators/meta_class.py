class Meta(type):
    def __new__(meta, classname, supers, classdict):
        ... Добавочная логика + создание объектов класса через обращение к type...
class C(metaclass= Meta):
    ... моя операция создания направляется Meta...  # подробно C = Meta('C', (), {...})