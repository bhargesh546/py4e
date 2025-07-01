import sqlite3

conn = sqlite3.connect('ages_tabledb.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Ages;
    
    CREATE TABLE Ages( 
                  name VARCHAR(128), 
                  age INTEGER );

    DELETE FROM Ages;
                  
    INSERT INTO Ages (name, age) VALUES ('Jay', 34), ('Eirian', 15), 
                                        ('Elvin', 35), ('Jacki', 31),
                                        ('Justine', 38), ('Erin', 29);
''')

cur.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')
print('First hex value:', cur.fetchone()[0])
conn.commit()