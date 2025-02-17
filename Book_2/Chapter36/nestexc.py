def action2():
    print(1 + [])   # Генерирует TypeError
def action1():
    try:
        action2()
    except TypeError:       # Самый последний совпадающий try внутренний оператор try
        print('inner try')
try:
    action1()
except TypeError:           # Здесь только в случае повторной генерации исключения в action1
                            # внешний оператор try
    
    print('outer try')