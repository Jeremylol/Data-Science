import pandas as pd

baseball_data = pd.read_csv('Master.csv')
# add values in two columns and write to a new csv file
baseball_data['height_plus_weight'] = baseball_data['height'] + baseball_data['weight']
baseball_data[['nameLast', 'nameGiven', 'height_plus_weight']].to_csv('heightplusweight.csv')
#create a new csv file with fullname
# 'Hetti' 'Suranga' -> 'Suranga Hetti'
baseball_data['fullname'] = baseball_data['nameGiven'] + ' ' + baseball_data['nameLast']
baseball_data[['fullname', 'birthCountry']].to_csv('playerLocation.csv', index = False)
# Find how many players are from Venezuela
ven_count = baseball_data['birthCountry'].value_counts()['Venezuela']
#print(ven_count)

#quiz 2
player_data = pd.read_csv('players.csv')
number_Of_Players = player_data['name'].count()
youngest_player = player_data['birthdate'].max()
youngest_player_name = player_data['name'][player_data['birthdate'] == youngest_player]
most_countries = player_data['country_id'].value_counts().iloc[:1]
print('Number of players:',number_Of_Players,'\nYoungest player:', youngest_player_name, '\nMost countries:', most_countries)
