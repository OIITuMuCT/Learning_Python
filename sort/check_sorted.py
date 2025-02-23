def check_sorted(A, ascending=True):
    """ Проверка упорядоченности по возрастанию за О(Len(A)) """
    flag = True
    s = 2* int(ascending) - 1
    N = len(A)
    for i in range(0, N-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag


print(check_sorted([1, 2, 3,]))