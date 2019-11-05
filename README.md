# N-Queens-Puzzle

This is a solution to the N-Queens puzzle using Python 3. 
It is important to run the code in an environment with Python 3, SQLAlchemy, Pandas and Pytest installed.

This code uses PostgreSQL through SQLAlchemy to store the solutions for each N from 8 to 14, so it is also important to
install PostgreSQL 12. To configure the database, I created a local server called "local" and then a database called
"queens", with port 5432, username "postgres" and password "password". You'll need to do the same if you want to run the
code straight away; otherwise, you can modify this information in 'queens4.py' on line 81, where the connection
to the database is set.

The code iterates through values of N from 8 to 14, since 14 was the highest N with processing time within 10 minutes.
To run the code, go to the terminal, be sure to run an environment where you have previously installed the specifications given
and to be located in the directory where you stored the files included in this repository.
Run the command "python queens4.py". To run the test cases, simply use the command "pytest".

The solutions stored are in a compressed format, in form of a list: each number represents the column where a queen is placed
for each row of the board from top to bottom, since we already know that each queen has to be placed in a different row.

IMPORTANT: The original core algorithm to find solutions for the queens puzzle was obtained from Solarian Programmer 
(sol-prog) [https://github.com/sol-prog/N-Queens-Puzzle] This code was modified to iterate through each value of N and to
store the solutions using PostgreSQL.

Manuel Salvador Cabrera Sanchez.
Last update: November 5, 2019.
Mexico City
