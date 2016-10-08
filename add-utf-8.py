# coding=utf-8

import sqlite3

conn = sqlite3.connect(r'/home/[user name]/.nixnote/db-1/nixnote.db')
# please replace r'/home/[user name]/.nixnote/db-1/nixnote.db' with r'/your/path/to/nixnote.db'

cur = conn.cursor()

cur.execute('SELECT lid FROM DataStore WHERE key = 5002', )
a = cur.fetchall()  # a = [(lid1,), (lid2,), ...]
a = [tup[0] for tup in a]

Todo_list = []  # will contain (lid, 'r' or 'b')

for lid in a:
    cur.execute(
        "SELECT data FROM DataStore WHERE key = 5002 AND lid = ?"
        , (lid,))
    data = cur.fetchone()[0]
    if data[0:5] == b'<?xml' or data[0:5] == r'<?xml':
        continue
    if data[0:5] == b'<!DOC' or data[0:5] == b'<!doc':
        Todo_list.append((lid, 'b'))
        data = b'<?xml version="1.0" encoding="UTF-8"?>' + data
        cur.execute( \
            "UPDATE DataStore SET data = ? WHERE key = 5002 AND lid = ?" \
            , (data, lid))
        # break
    elif data[0:5] == r'<!DOC' or data[0:5] == r'<!doc':
        Todo_list.append((lid, 'r'))
        data = r'<?xml version="1.0" encoding="UTF-8"?>' + data
        cur.execute( \
            "UPDATE DataStore SET data = ? WHERE key = 5002 AND lid = ?" \
            , (data, lid))
        # break
    else:
        continue
conn.commit()
# print(Todo_list)
