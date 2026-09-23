
import sqlite3

# Connect Python to the SQLite database file.
connection = sqlite3.connect("school.db")
# A cursor is the object that sends SQL commands to the database.
cursor = connection.cursor()

# Execute SQL to create the students table if it does not exist yet.
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    year_group INTEGER,
    criminal_record TEXT
)
""")

# Clear old rows so this lesson script gives predictable output each run.
cursor.execute("DELETE FROM students")

# Insert rows using placeholders (?) to safely pass Python values.
cursor.execute("INSERT INTO students (name, year_group, age) VALUES (?, ?, ?)", ("Ava", 10, 16))
cursor.execute("INSERT INTO students (name, year_group, age, criminal_record) VALUES (?, ?, ?, ?)", ("Leroy", 34, 45, "Wanted for Terrorism"))
cursor.execute("INSERT INTO students (name, year_group, age, criminal_record) VALUES (?, ?, ?, ?)", ("Elliot Alderson", 32, 28, "Computer Fraud and Abuse, Money Laundering, Wire Fraud, Identity Theft, Computer Intrusion, Conspiracy to Murder, Phishing, Illegal Access to Private Data Servers, Trespassing, Unauthorised access, modification, or impairment of computer data/communications, Dishonestly obtaining or dealing in personal financial information, Extortion and Blackmail"))

# Commit saves all changes made by INSERT/DELETE/CREATE statements.
connection.commit()
# Always close the connection when finished.
connection.close()