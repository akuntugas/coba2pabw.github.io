import sqlite3

conn = sqlite3.connect("wilayah.db")
cursorObj = conn.cursor()
cursorObj.execute ('''

    UPDATE alamat set nama ="iqbal" where id="2"

''')

conn.commit()
conn.close()