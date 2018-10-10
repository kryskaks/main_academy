import sqlite3


# you need to create table in sqlite3 console using SQL,
# ~/projects/main_academy$ sqlite3 test.db
# create table persons (id int, name varchar(20));
# and create new records in it
# insert into persons values(1, 'Jack');


conn = sqlite3.connect('test.db')

cur = conn.cursor()

cur.execute("select name, id from persons where id = %s")


rows = cur.fetchall()

for row in rows:
    print(row, type(row))


conn.close()
