def makeActions():
    acts = []
    for i in range(5):                      # Использование стандартных значений
        acts.append(lambda x, i=i: i**x)    # Запоминает текущее значение i
    return acts

acts = makeActions()
print(acts[0](2))   # 0 ** 2
print(acts[1](2))   # 1 ** 2
print(acts[2](2))   # 2 ** 2
print(acts[3](2))   # 3 ** 2
print(acts[4](2))   # 4 ** 2
