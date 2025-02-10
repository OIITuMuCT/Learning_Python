from converters import Uppercase

class HTMLize:
    def write(self, line):
        print(f'<PRE>{line.rstrip()}<PRE>')

if __name__ =='__main__':
    rec = Uppercase(open('trispam.txt'),  HTMLize() ).process()
