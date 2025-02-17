# Базовое использование with as
# with выражение [as переменная]:
#     блок-with
with open('trispam.txt') as myfile:
    for line in myfile:
        print(line)
        # ...дополнительный код...

myfile = open('tispamup.txt')
try:
    for lane in myfile:
        print(line)
        # ...дополнительный код...
finally:
    myfile.close()
