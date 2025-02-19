#!python
""" 
classtree.py: подъем по деревьям наследования с применением связей между 
пространствами имен и отображением находящихся выше суперклассов с отступом
согласно высоте
"""
def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent+3)

def instancetree(inst):
    print(f'Tree of {inst}')
    classtree(inst.__class__, 3)

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    class E: pass
    class F(D,E): pass
    # instancetree(A())
    instancetree(B())
    # instancetree(C())
    # instancetree(D())
    # instancetree(E())
    instancetree(F())

if __name__ == "__main__": selftest()
