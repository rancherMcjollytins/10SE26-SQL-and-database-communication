import _sqlite3

connectionVar =  _sqlite3.connect("school.db")

SQLCursor = connectionVar.cursor()

year_group_filter = 10