# Простая фабричная функция

def maker(N):

    def action(X):      # Создание и возвращение функции action
        return X ** N   # action сохраняет N из объемлющей области видимости

    return action

if __name__ == '__main__':
    f = maker(2)    # Передача 2 аргументу N
    print(f)        # <function maker.<locals>.action at 0x7a312cf8e7a0>
    print(f(3))     # Передача 3 аргументу X, в N запоминается 2: 3 ** 2
    print(f(4))     # Передача 3 аргументу X, в N запоминается 2: 4 ** 2
