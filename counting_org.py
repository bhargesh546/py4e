import sqlite3

conn = sqlite3.connect('email_orgdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Counts;
    
    CREATE TABLE Counts (org TEXT, count INTEGER);              
''')

file = input("Enter the file name: ")
if len(file) < 1:
    file = "mbox.txt"

fh = open(file)
for line in fh:
    if not line.startswith('From: '):
        continue

    pieces = line.strip().split()
    email = pieces[1].split('@')[1]
    cur.execute('''SELECT count FROM Counts WHERE org = ?''', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts(org, count) VALUES(?, 1)''',(email, ))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (email, ))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for line in cur.execute(sqlstr):
    print(line)

cur.close()