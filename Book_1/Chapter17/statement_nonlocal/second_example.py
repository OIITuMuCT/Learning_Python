def intersection(seq1, seq2):
    res = []                # Начать с пустого результата
    for x in seq1:          # Просмотр seq1
        if x in seq2:       # Общий элемент?
            res.append(x)   # Добавить в конец результата
    return res


if __name__ == '__main__':
    s1 = 'SPAM'
    s2 = 'SCAM'
print(intersection((1, 2, 3, 4), (3, 4, 5)))
print(intersection(s1, s2))
print([x for x in s1 if x in s2])