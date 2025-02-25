def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)
                # Перехватывать и делегировать встроенные операции особым образом
                def __str__(self):
                    return str(self.__wrapped)
                def __add__(self, other):
                    return self.__wrapped + other           # или getattr(x, '__add__')(y)
                def __getitem__(self, index):
                    return self.__wrapped[index]            # При необходимости
                def __call__(self, *args, **kwargs):
                    return self.__wrapped(*args, **kwargs) # При необходимости
                # плюс любые другие, которые нужны
                
                # перехватывать и делегировать доступ к атрибутам
                # по имени обобщенным образом
                def __getattr__(self, attr):...
                def __setattr__(self, attr, value):...
        return onInstance
    return onDecorator