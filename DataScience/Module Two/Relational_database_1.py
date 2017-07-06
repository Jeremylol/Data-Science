import pandas as pd
import sqlite3
from datetime import datetime

conn = sqlite3.connect("flights.db")
df = pd.read_sql_query("select * from routes limit 5",conn)
print(df)
# insert tuple to a table in the db
cur = conn.cursor()
cur.execute("insert into airlines values(6048,19846,'Test flight','','',null,null,null, 'Y')") # execute(insert...) generates a flight.db journal
conn.commit()
print(pd.read_sql_query("select * from airlines where id=19846",conn))
#update a tuple
values = ('USA', 19846)
cur.execute("update airlines set country = ? where id= ?", values)
conn.commit()
print(pd.read_sql_query("select * from airlines where id=19846",conn))
# delete a tuple
cur.execute("delete from airlines where id= 19846")
conn.commit()
print(pd.read_sql_query("select * from airlines where id=19846",conn)) #empty dataframe ???????? didn't finish working.
#create new table
# --->>cur.execute("create table my_daily_flights(id integer, departure date, arrival date, number text, route_id integer)")
conn.commit()
cur.execute("insert into my_daily_flights values(1, '2017-05-18 3:35', '207-05-19 9:55', 'T1', 1)")
conn.commit()
print(pd.read_sql_query("select * from my_daily_flights"),conn)
#create table with pandas data frame.
flightdf = pd.DataFrame([[1, datetime(2017, 0o5, 17, 3, 35), datetime(2017, 0o5, 19, 9, 55), 'T1', 1]], columns=["id", "departure", "arrival", "number", "route-id"])
#convert dataframe to a table, replace if it exists
flightdf.to_sql("another_daily_flights",conn,if_exists= "replace")
print = (pd.read_sql_query("select * from another_daily_flights",conn))
#alter the table, no commit necessary
cur.execute("alter table another_daily_flights add column airplanes integer")
