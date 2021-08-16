import sqlite3


conn = sqlite3.connect("test.db")
curr = conn.cursor()

curr.execute('''CREATE TABLE students 
                (name text, roll text)''')

curr.execute("INSERT INTO students VALUES ('gopal', '17')")
conn.commit()
conn.close()
