def timer(label=''):
    def decorator(func):

        def onCall(*args):          # Многоуровневое предохранение состояния:
            ...                     # аргументы передаются функции
            func(*args)             # func хранится в объемлющей области видимости
            print(label, ...)       # label хранится в объемлющей области видимости

        return onCall               # Возвращается действительный декоратор
    return decorator


@timer("==>")                       # Подобно listcomp = timer ('==>') (listcomp)
def listcomp(N): ...                # list comp повторно привязывается
                                    # к новой функции onCall

listcomp(...)                       # В действительности вызывается onCall
