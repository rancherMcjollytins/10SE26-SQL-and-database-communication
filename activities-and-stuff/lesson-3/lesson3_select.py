import sqlite3

connectionVar = sqlite3.connect("school.db")
#cursor runs SQL queries and returns results in python
cursor = connectionVar.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    year_group INTEGER,
    criminal_record TEXT
)
""")
#both this and the other work btw
#cursor = sqlite3.Cursor(connectionVar)


#Run a SELECT query to read columns
cursor.execute("SELECT id, name, age, year_group, criminal_record FROM students")
#fetchall() returns a list of all rows from the most recent query
fetched_rows = cursor.fetchall()
for row in fetched_rows:
    print(row)

# Each row is a tuple (id, name, year_group) 
# just needed google ai and stackflow help for better formatting
for row_id, name, age, year_group, criminal_record in fetched_rows:
    print(f"| Student ID: {row_id} || Name: {name} || Age: {age} || Year: {year_group} || Criminal Record: {criminal_record} |")

# alwatys remember
connectionVar.close()