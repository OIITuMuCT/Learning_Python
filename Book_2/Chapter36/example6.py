""" Закрытие файлов и серверных подключений """

myfile = open('path/filename.txt', 'w')
try:
    ...обработка myfile...
finally:
    myfile.close()


# Традиционная форма
myfile = open('filename', 'w')

myfile.close()

# Форма с диспетчером контекста
with open('filename') as myfile:
    обработка myfile