class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file
def parser():
    raise FormatError(42, file='spam.txt')
try:
    parser()
except FormatError as X:
    print('Error at: %s %s' % (X.file, X.line))
