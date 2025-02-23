import time
def timer(label='', trace=True):   
    """При аргументах декоратора: сохранение аргументов """
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kwargs):
            start = time.time()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                falues = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer