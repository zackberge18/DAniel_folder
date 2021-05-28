# Send info to my plate button
# create plate database and re run func so that it create and going to except part
# create or open
import sqlite3
conn = sqlite3.connect("my_plate.db")
# create a cursor
c = conn.cursor()
# Operation
c.execute("""CREATE TABLE student_info (         my_id integer,
                                                 id integer,
                                                 name text,
                                                 food text)""")
# commit changes
conn.commit()
# close the connection
conn.close()
# send food to my plate db