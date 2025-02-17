# for pair in zip(open('script1.py'), open('script2.py')):
#     print(pair)
with open('script2.py') as fin, open('upper.py', 'w') as fout:
    for line in fin:
        fout.write(line.upper())
print(open('upper.py').read())

fin = open('script2.py')
fout = open('lower.py', 'w')
try:
    for line in fin:
        fout.write(line.lower())
finally:
    fin.close()
    fout.close()