"""Lesson 1: Connect to a SQLite database file."""

import sqlite3

print("The script creates a connection to a database called school.db, stored in a connection-variable called 'connection'. \nIf the database 'school.db' can't  be found (e.g. if we rename it to library), it will create the school.db file.")

# Open a connection to school.db (SQLite creates the file if needed).
connection = sqlite3.connect("school.db")
print("Database connected!")
# Close the connection so the file is safely released. :D 
connection.close()
print("Database closed!") 