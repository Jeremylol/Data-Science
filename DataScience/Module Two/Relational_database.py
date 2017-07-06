import pandas as pd
import pandasql
import sqlite3

aadhaar_data = pd.read_csv('aadhaar_data.csv')
aadhaar_data.rename(columns = lambda x: x.replace(' ','_').lower(), inplace = True)
# use SQLite syntax
q = "SELECT * FROM  aadhaar_data LIMIT 20"   # * means "all"
sqlsolution = pandasql.sqldf(q.lower(),locals())
print(sqlsolution)
q2 = "SELECT district, sub_district, Sum(aadhaar_generated) FROM aadhaar_data WHERE age > 50 GROUP BY district, sub_district"
sqlsolution2 = pandasql.sqldf(q2.lower(),locals())
print(sqlsolution2)
# www.SQLite.org to find documentation
#Create a connection object
con = sqlite3.connect("flights.db")  # flights database ->   airlines/ airports / routes
#create cursor for executing queries
cur = con.cursor()
#execute a query
cur.execute("SELECT * from airlines limit 5")
results = cur.fetchall() # extract data from cursor object
print(results)
cur.execute("select name, city from airports group by country")
airports = cur.fetchall()
print(airports)
df1 = pd.read_sql_query("select * from routes limit 5",con)
print(df1)
# insert tuple to a table in the db
cur.execute("insert into airlines values(6048,19846,'Test flight','','',null,null,null, 'Y')") # execute(insert...) generates a flight.db journal
con.commit()
print(pd.read_sql_query("select * from airlines where id=19846",con))
cur.close()
con.close() #unlock database