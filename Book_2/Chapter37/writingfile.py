name = 'Bob'
job = 'mgr'
date = '12/01/24'

with open('testfile', 'w') as fout:
    fout.write(f'{name}, {job}, {date} , [123, 112, 120, 97]')
    fout.read()
    fout.close()

