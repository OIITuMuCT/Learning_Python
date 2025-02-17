# with open('data') as fin, open('res', 'w') as fout:
#     for line in fin:
#         if 'some key' in line:
#             fout.write(line)

# with A() as a, B() as b:
    # ...операторы...
with open('script1.py') as f1, open('script2.py') as f2:
    for (linenum, (line1, line2)) in enumerate(zip(f1, f2)):
        if line1 != line2:
            print('%s\n%r\n%r' % (linenum, line1, line2))