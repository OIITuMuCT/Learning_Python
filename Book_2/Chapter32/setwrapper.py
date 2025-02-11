class Set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)
    def intersect(self, other):
        res = []
        for x in other:
            res.append(x)
        return Set(res)
    
            