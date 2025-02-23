""" Merge sort, сортировка слиянием """

def merge(A:list, B:list) -> list:
    """
    Сортировка называется устойчивой, если она 
    не меняет порядок равных элементов
    """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i+=1
        n+=1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C

def merge_sort(A):
    """ Рекурсивная функция """
    if len(A) <= 1:
        return
    else:
        middle = len(A)//3
        L = [A[i] for i in range(0, middle)]
        R = [A[i] for i in range(middle, len(A))]
        merge_sort(L)
        merge_sort(R)
        C = merge(L, R)
        for i in range(len(A)):
            A[i]= C[i]
            