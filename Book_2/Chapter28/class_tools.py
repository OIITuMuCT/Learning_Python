class AttrDisplay:
    """
    Представляет наследуемый метод перезагрузки отображения, который показывает
    экземпляры с их именами классов и пары имя=значение для каждого атрибута, 
    сохраненного в самом экземпляре (но не атрибутов унаследованных от его классов).
    Может соединяться с любым классом и будет работать на любом экземпляре.
    """
    def getherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.getherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2
    class SubTest(TopTest):
        pass
    X , Y = TopTest(), SubTest()
    print(X)
    print(Y)