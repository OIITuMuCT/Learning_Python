"""
Пример написания кода действий при завершении с помощью try/finally
"""


class MyError(Exception):
    pass

def stuff(file):
    raise MyError()

file = open("data", "w")  # Открытие выходного файла

# (также может потерпеть неудачу)

try:
    stuff(file)
finally:
    file.close()

print("not reached")
