while True:
    try:
        line = input()
        print(line[::-1].upper())
    except EOFError:
        break
    else:
        print('enter end for exit')
        if line =='end':
            break
    # ...обработка очередной строки...