import sqlite3

conn = sqlite3.connect("kebo.db")

cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(100))"
# cursor.execute(query)

# TO INSERT VALUES

# query = "INSERT INTO sys_command VALUES (null,'One Note', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Program\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Dont forget to close the connection when done 

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(100))"
# cursor.execute(query)

# # TO INSERT VALUES

# query = "INSERT INTO web_command VALUES (null,'Youtube', 'https://youtube.com')"
# cursor.execute(query)
# conn.commit()
# conn.close()  # Dont forget to close the connection when done 




# Testing Module
# query = "OneNote"
# cursor.execute('SELECT path FROM sys_command WHERE name IN(?)',(query,))
# results = cursor.fetchall()
# print(results[0][0])