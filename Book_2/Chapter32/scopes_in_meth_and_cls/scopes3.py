def generate(label):
    class Spam:
        count = 1
        def method(self):
            print('%s=%s' % (label, Spam.count))
    return Spam


if __name__ == '__main__':
    aclass = generate('Cotchas')
    I = aclass()
    I.method()
    print(I.__class__.__name__)
    print(I.__getattribute__)