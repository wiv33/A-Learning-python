import sqlite3

conn = sqlite3.connect('userTable')

cs = conn.cursor()
result = cs.execute('SELECT * FROM userTable')

print(result)