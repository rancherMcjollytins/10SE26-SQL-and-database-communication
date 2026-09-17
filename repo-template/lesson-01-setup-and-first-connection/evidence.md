# Lesson 01 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: 
25c385a : Files made
    >made some files and folders to store the activities, ran them and also changed name of 'school.db' to 'library.db'.
    Outputs the correct output, showing a connection is made and creates a school.db file if original is renamed or 
    deleted.
    >
- Commit 2 hash + message:
- Optional Commit 3 hash + message:

## Run evidence
- Command run (example: `python lesson1_connect.py`):
- Terminal output pasted below:
```bash
PS C:\Users\adrian.uy\Documents\GitHub\10SE26-SQL-and-database-communication\10SE26-SQL-and-database-communication> & "C:\Program Files\Python314\python.exe" c:/Users/adrian.uy/Documents/GitHub/10SE26-SQL-and-database-communication/10SE26-SQL-and-database-communication/activities-and-stuff/lesson-1/lesson1_connect.py
```
```
The script creates a connection to a database called school.db, stored in a connection-variable called 'connection'. 
If the database 'school.db' can't  be found (e.g. if we rename it to library), it will create the school.db file.
Database connected!
Database closed!
PS C:\Users\adrian.uy\Documents\GitHub\10SE26-SQL-and-database-communication\10SE26-SQL-and-database-communication> 
```

## What I changed from the starter example
- I renamed school.db to library.db, which made the script unable to find school.db, thus it made a new file named 'school.db' which it made a connection to.

## Error and fix
- Error I hit: lesson1_connect.py not found
- How I fixed it: Since I moved the script into a folder for activities, I had to enter the relative path (activities-and-stuff\lesson-1\lesson1_connect.py) as it was in the same repo, but a specific folder.

## Understanding check (answer in your own words)
1. What is the difference between Python and SQLite? Python is a high-level programming language for general programming, providing support for a diverse range of programs. SQLite is a database engine that stores databases in files. Python and SQLite can interact using the sqlite3 python module.
2. What file was created when the script ran?
When the script ran, it created a file called 'school.db'. Once school.db was created, it just connected to that file when run again, however, when renamed to 'library.db', it could not find and connect with 'school.db' thus, it created a new school.db file.
3. What does the connection do?

## Quality checklist
- [X] Script runs without unhandled errors
- [ ] I included at least 2 lesson commits
- [X] I included terminal evidence
- [ ] I answered all questions in my own words
