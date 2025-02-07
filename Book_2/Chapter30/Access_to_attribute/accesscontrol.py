import sqlite3

def main():
    s= sqlite3.connect('mydb')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE Accesscontrol''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()