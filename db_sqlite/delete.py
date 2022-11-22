import sqlite3

conn = sqlite3.connect("wilayah.db")
cursorObj = conn.cursor()
cursorObj.execute ('''
    delete from alamat where id="1"
''')

conn.commit()
conn.close()