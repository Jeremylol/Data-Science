import json
import requests

url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=4005c05d541d9a056136d5450be12883&artist=Rihanna&album=loud&format=json'
data = requests.get(url).text
data = json.loads(data)
print(data)
print('readable :', json.dumps(data, indent = 4))
# read just a piece of information
print(data['album']['listeners'])
# find the top artist in spain and the # of top listeners
url1 = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&api_key=4005c05d541d9a056136d5450be12883&country=spain&limit=1&format=json'
data1 = requests.get(url1).text
data1 = json.loads(data1)
print(json.dumps(data1, indent=4))
print(data['topartists']['artists'][0]['listeners'])