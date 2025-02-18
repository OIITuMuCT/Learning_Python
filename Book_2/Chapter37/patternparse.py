import re
text = open('mybooks.xml', 'r').read()
found = re.findall('<title>(.*)</title>', text)
for title in found:
    print(title)