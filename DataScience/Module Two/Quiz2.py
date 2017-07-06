import pandas as pd

player_data = pd.read_csv('players.csv')
number_Of_Players = player_data['name'].count()
youngest_player = player_data['birthdate'].max()
youngest_player_name = player_data['name'][player_data['birthdate'] == youngest_player]
most_countries = player_data['country_id'].value_counts().iloc[:1]
print('Number of players:',number_Of_Players,'\nYoungest player:', youngest_player_name, '\nMost countries:', most_countries)