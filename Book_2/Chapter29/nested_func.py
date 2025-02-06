def function1():  # Первая функция
    print("Hello World!")

    def function2():  # Функция которую нужно вызвать из первой функции.
        print("World is answer: Hello!")

    return function2


function1()  # вызываем внешнюю функцию, возврат игнорируем
function1()()  # вызываем внешнюю функцию, возврат вызываем как функцию
