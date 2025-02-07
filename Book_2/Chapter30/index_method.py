class C:
    def __index__(self):
        return 255


X = C()
print(hex(X))
print(bin(X))
print(oct(X))
print(('C'*256)[255])
