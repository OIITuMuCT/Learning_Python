class MixedNames:
    data = 'spam'
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data, MixedNames.data)

if __name__ == '__main__':
    mix = MixedNames('Eggs')
    mix.display()