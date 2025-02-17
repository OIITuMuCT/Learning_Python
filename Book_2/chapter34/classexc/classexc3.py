class MyBad(Exception):
    def __str__(self):
        return 'Always look on the bright side of life...'

try:
    raise MyBad()
except MyBad as X:
    print(X)