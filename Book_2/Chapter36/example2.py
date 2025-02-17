
class Exitloop(Exception):
    """
    Прерывание множества вложенных циклов: "безусловный переход" 
    """
    pass


try:
    while True:
        while True:
            for i in range(10):
                if i > 3: 
                    raise Exitloop
                
                print('loop3: %s' % i)
            print('loop2')
        print('loop1')
except Exitloop:
    print('continuing')