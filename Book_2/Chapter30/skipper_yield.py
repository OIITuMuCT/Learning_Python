class SkipperObject:                    # Еще один генератор на основе__ iter__ + yield
    def __init__(self, wrapped):        # Область видимости экземпляра сохраняется нормально
        self.wrapped = wrapped          # Состояние локальной области видимости сохраняется
                                        # автоматически

    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item
