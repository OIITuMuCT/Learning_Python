def intersection(seq1, seq2):
    res = []                # Начать с пустого результата
    for x in seq1:          # Просмотр seq1
        if x in seq2:       # Общий элемент?
            res.append(x)   # Добавить в конец результата
    return res

print(intersection((1, 2, 3, 4), (3, 4, 5)))
