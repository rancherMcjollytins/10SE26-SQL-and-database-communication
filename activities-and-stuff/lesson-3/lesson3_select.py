import sqlite3

connectionVar = sqlite3.connect("school.db")
#cursor runs SQL queries and returns results in python
cursor = connectionVar.cursor()

#both this and the other work btw
#cursor = sqlite3.Cursor(connectionVar)


#Run a SELECT query to read columns
cursor.execute("SELECT id, name, year_group FROM students")
#fetchall() returns a list of all rows from the most recent query
fetched_rows = cursor.fetchall()

# Each row is a tuple (id, name, year_group) 
# just needed google ai and stackflow help for better formatting
for row_id, name, age in fetched_rows:
    print(f"Student ID: {row_id} || Name: {name} || Age: {age}")

connectionVar.close()