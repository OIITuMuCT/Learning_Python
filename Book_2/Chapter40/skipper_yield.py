class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset +=1
            yield item

if __name__ == '__main__':
    skipper = SkipObject('Hello bro')
    I = iter(skipper)

    # for i in I:
    #     print(i, end=' ')
    print(next(I))