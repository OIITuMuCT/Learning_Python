import time
def timer(func):
    """Показывает время работы программы"""

    def wrapped(*args, **kwargs):
        start = time.time()
        print("запуск...", start)
        print(func(*args, **kwargs))
        print("завершение...", round((time.time() - start), 5))
        return func(*args, **kwargs)
    return wrapped
@timer
def func(x, y):
    return x ** y

@timer
def insert_sort(A):
    """Сортировка списка А вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1
@timer
def choice_sort(a):
    n = len(a)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if a[pos] > a[k]:
                a[pos], a[k] = a[k], a[pos]
    return a

@timer
def quick_sort(a:list):
    pivot = a[0]
    for i in range(len(a)-1):
        k = 0
        if pivot > a[i]:
            a[k], pivot = pivot, a[k]
            pivot = a[k+1]
        else:
            k += 1
    return a

a = [6,5,1,3,8,4,7,9,2]
# quick_sort(a)
choice_sort(a)
import random
from random import shuffle
b = [x for x in range(random.randint(20, 100))]
shuffle(b)
print(choice_sort(b))
print(b)