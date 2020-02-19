import sqlite3

connection=sqlite3.connect("flights_travilig.db")
c=connection.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS flights (id SERIAL PRIMARY KEY,origin VARCHAR NOT NULL,\
        destination VARCHAR NOT NULL, duration INTEGER NOT NULL)")


create_table()

def dataentry():
    c.execute("INSERT INTO flights (origin, destination, duration)\
      VALUES ('New York', 'London', 415);")
    c.execute("INSERT INTO flights (origin, destination, duration)\
    VALUES ('London', 'Brazil', 450);")
    c.execute("INSERT INTO flights (origin, destination, duration)\
    VALUES ('Angola', 'New York', 456);")
    c.execute("INSERT INTO flights (origin, destination, duration)\
    VALUES ('Brazil', 'Angola', 500);")
    
    connection.commit()

dataentry()