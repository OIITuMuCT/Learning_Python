import shelve

db = shelve.open('persondb')

if __name__ == '__main__':
    print(len(db))
    print(list(db.keys()))
    bob = db["Bob Smith"]
    print(bob)
    print(bob.lastName())
    for key in db:
        print(key , '=>', db[key])