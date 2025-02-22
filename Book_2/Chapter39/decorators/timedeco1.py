import time, sys
force = list if sys.version_info[0] == 3 else (lambda X: X)

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        elapsed = time.time() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]
@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))


if __name__ == '__main__':

    result = listcomp(5)

    listcomp(50000)
    listcomp(500000)
    listcomp(1000000)
    # listcomp(10000000)
    print(result)
    print('alltime = %s' % listcomp.alltime)
    print('')
    result = mapcall(5)
    mapcall(50000)
    mapcall(500000)
    mapcall(1000000)
    # mapcall(10000000)

    print("\n**map/comp = %s" % round(mapcall.alltime / listcomp.alltime, 3))
