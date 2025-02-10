class adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


class addboth(adder):
    def __str__(self):
        return f"[Value: {self.data}]"

    def __repr__(self):
        return f"addboth({self.data})"

if __name__ == '__main__':
    x = addboth(4) 
    x = x+1
    print(str(x))
    # код работает только в интерпретаторе


