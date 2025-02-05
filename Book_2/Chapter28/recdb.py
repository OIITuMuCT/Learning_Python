import shelve
db = shelve.open('persondb')
rec = db['Sue Jones']

print(rec)
print(rec.pay)
print(rec.lastName())