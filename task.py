from dbm import _Database
import sqlite3

#database created

import sqlite3
from tokenize import Name
conn=sqlite3.connect('Movies.db')
print("database conected")

# Table Created

conn.execute('''''CREATE TABLE Movies
(Name Text Not Null
actor Text Not Null
actress Text Not Null
director Text Not Null
year of release Text Not Null); ''''')

print("Table created sucessfully")

# record inserted

conn.execute("insert into Movies (Name, actor, actress, director, year of release)values(sharesha,shidharyt,aadi,2021;)")
conn.execute("insert into Movies (Name, actor, actress, director, year of release)values(sharesha,shidharyt,aadi,2021;)")


# select record
data=conn.execute("select * from Movies ")
print("Name = " ,row[0])
print("Actor =",row[1])
print("Actress =",row[2])
print("Director =",row[3])
print("year of release =",row[4])
