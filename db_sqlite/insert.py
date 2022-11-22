import sqlite3

conn = sqlite3.connect("wilayah.db")
cursorObj = conn.cursor()
cursorObj.execute('''
        INSERT INTO alamat (nama,alamat) VALUES ("adi" , "sidoarjo");
''')

conn.commit()
conn.close()