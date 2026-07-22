import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE students(
    id INTEGER,
    name TEXT,
    age INTEGER
)
""")


cursor.execute("SELECT * FROM students")
student = cursor.fetchone()
manystudents = cursor.fetchmany(2)
students = cursor.fetchall()
print(student)
print(students)
print(manystudents)

for student in students:
    print(student)

for id, name, age in students:
    print(name, age)


id = 1
name = "Alice"
age = 20

cursor.execute(
    "INSERT INTO students VALUES (?, ?, ?)",
    (id, name, age)
)


student_id = 2

cursor.execute(
    "SELECT * FROM students WHERE id = ?",
    (student_id,)
)


cursor.execute(
    "SELECT * FROM students WHERE name = ? AND age = ?",
    (name, age)
)


cursor.execute(
    "UPDATE students SET age = ? WHERE id = ?",
    (age, id)
)


student_id = 3

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (student_id,)
)


conn.commit()
conn.close()




# Connect
#    ↓
# Cursor
#    ↓
# Execute
#    ↓
# Commit
#    ↓
# Close



import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()


#Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    price INTEGER
)
""")


#Insert Into Table
cursor.execute(
"INSERT INTO books VALUES(?, ?, ?)",
    (1, "FastAPI Book", 700)
)

cursor.execute(
"INSERT INTO books VALUES(?, ?, ?)",
    (2, "REST APIs Book", 830)
)


#Read From Table
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

for id, name, price in books:
    print(id, name, price)


#Update In Table
cursor.execute(
"UPDATE books SET price = ? WHERE id = ?",
(711, 1)
)


#Delete From Table
cursor.execute(
"DELETE FROM books WHERE id= ?",
(1,)
)


conn.commit()
conn.close()