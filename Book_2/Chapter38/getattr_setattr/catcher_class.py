class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

if __name__ == '__main__':
    X = Catcher()
    X.job
    X.job = 'mgr'
    X.pay
    X.pay = 99