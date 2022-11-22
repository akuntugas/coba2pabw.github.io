import sqlite3

conn = sqlite3.connect("wilayah.db")
cursorObj = conn.cursor()
cursorObj.execute('''
    CREATE TABLE "alamat" (
        "ID"        integer not null unique,
        "nama"      text not null,
        "alamat"    text not null,
        primary key ("ID" autoincrement)
    );
''')

conn.close()