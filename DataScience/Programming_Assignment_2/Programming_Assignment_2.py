import pandas as pd
import pandasql
import json
import requests
import sqlite3


aadhaar_data = pd.read_csv('aadhaar_data.csv')
accepted = aadhaar_data['Aadhaar generated'].value_counts()[1] # Q 1
rejected = aadhaar_data['Enrolment Rejected'].value_counts()[1] # Q 2
males = aadhaar_data['Gender'].value_counts()['M'] # Q3
females = aadhaar_data['Gender'].value_counts()['F'] # Q3
# Q 4
aadhaar_data.rename(columns = lambda x: x.replace(' ','_').lower(), inplace = True)
lessThan25 = "SELECT Age FROM aadhaar_data WHERE age < 25"
between25and55 = "SELECT Age FROM aadhaar_data WHERE age >= 25 AND age <= 55"
over55 = "SELECT Age FROM aadhaar_data WHERE age > 55"
lessThan_25 = pandasql.sqldf(lessThan25.lower(),locals())
between_25and_55 = pandasql.sqldf(between25and55.lower(),locals())
over_55 = pandasql.sqldf(over55.lower(),locals())
total = lessThan_25.count() + between_25and_55.count() + over_55.count()
# Q 5
weather_data = pd.read_csv('weather_underground.csv')
weather_data.rename(columns = lambda x: x.replace(' ','_').lower(), inplace = True)
q = "SELECT COUNT(*) FROM weather_data WHERE rain == 1 "
sqlsolution = pandasql.sqldf(q.lower(),locals())
# Q 6
q1 = "SELECT fog, MAX(maxtempi) FROM weather_data GROUP BY fog"
fog = pandasql.sqldf(q1.lower(),locals())
# Q 7
q2 = " SELECT AVG(meantempi) FROM weather_data WHERE CAST(STRFTIME('%w', date) AS INTEGER) = 0 OR CAST(STRFTIME('%w', date) AS INTEGER) = 6 "
meanTemp = pandasql.sqldf(q2.lower(),locals())
'''
# Q 8
# find the top artist in India and the # of top listeners
url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&api_key=4005c05d541d9a056136d5450be12883&country=india&format=json'
data = requests.get(url).text
data = json.loads(data)
top_Artist_Name = data['topartists']['artist'][0]['name']
top_Artist_Listeners= data['topartists']['artist'][0]['listeners']

url1 = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&api_key=4005c05d541d9a056136d5450be12883&country=india&limit=1000&format=json'
data1 = requests.get(url1).text
data1 = json.loads(data1)
top_artists_all = data['topartists']['artist'][2]['name']
top_all_listeners = data['topartists']['artist'][0]['listeners']

con = sqlite3.connect("music.db")
cur = con.cursor()
cur.execute("create table opIndianListeners(artist text, number_of_listeners integer)")
con.commit()
value = (top_Artist_Name)
value1 = (top_Artist_Listeners)
cur.execute("insert into opIndianListeners values(?, ?)", (value, value1))
con.commit()
cur.execute("SELECT * from opIndianListeners")
'''
print('Number accepted: ',accepted)
print('Number rejected: ',rejected)
print('\n', males, 'Males +', females, 'Females  = ',(males + females), ' applicants ')
print('less than age 25:',lessThan_25.count(), '\nbetween 25 and 55:',between_25and_55.count(),'\nover 55:', over_55.count())
print('\ntotal number of applicants:',total)
print('\n',sqlsolution)
print('\n',fog)
print('\n',meanTemp)


