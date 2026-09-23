import _sqlite3

connectionVar =  _sqlite3.connect("school.db")

SQLCursor = connectionVar.cursor()

year_group = 10
SQLCursor.execute(
    "SELECT year_group FROM STUDENTS WHERE year_group = ? ORDER BY year_group",
    (year_group,)
)


rows = SQLCursor.fetchall()
for row in rows:
    print(row)

SQLCursor.execute("SELECT COUNT(*) FROM students")
total_students = SQLCursor.fetchone()[0]
print("Total Students:", total_students)

"""
# for ranges according to gemini so be careful with ai code!!!!!!

min_year = 6
max_year = 32
SQLCursor.execute(
    "SELECT name, year_group FROM STUDENTS WHERE year_group BETWEEN ? AND ? ORDER BY NAME",
    (min_year, max_year)
)

rows2 = SQLCursor.fetchall()
for row2 in rows2:
    print(row2)

"""
connectionVar.close()