import pandas as pd
import numpy as np

# Part 1
data = {'gold':pd.Series([13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        index = ['Russian Fed.', 'Norway', 'Canada', 'United States',
'Netherlands', 'Germany', 'Switzerland', 'Belarus',
'Austria', 'France', 'Poland', 'China', 'Korea',
'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']),
        'silver':pd.Series([11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0],
        index = ['Russian Fed.', 'Norway', 'Canada', 'United States',
'Netherlands', 'Germany', 'Switzerland', 'Belarus',
'Austria', 'France', 'Poland', 'China', 'Korea',
'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']),
        'bronze':pd.Series([9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1],
        index = ['Russian Fed.', 'Norway', 'Canada', 'United States',
'Netherlands', 'Germany', 'Switzerland', 'Belarus',
'Austria', 'France', 'Poland', 'China', 'Korea',
'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']) }

olympic_medal_counts_df = pd.DataFrame(data, columns= ['gold','silver','bronze'])
print(olympic_medal_counts_df)

# Part 2
avg_bronze_at_least_one_gold = olympic_medal_counts_df['bronze']
print('\n\tBronze average is =', np.average(avg_bronze_at_least_one_gold))

# Part 3
avg_medal_count = olympic_medal_counts_df.apply(np.average)
print('\n',avg_medal_count)

# Part 4
CountryNames = ['Russian Fed.', 'Norway', 'Canada', 'United States',
'Netherlands', 'Germany', 'Switzerland', 'Belarus',
'Austria', 'France', 'Poland', 'China', 'Korea',
'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
gold1 = np.dot(4,gold)
silver1 = np.dot(2,silver)
bronze1 = np.dot(1,bronze)
numbers = gold1 + silver1 + bronze1

dataSet = list(zip(CountryNames,numbers))
olympic_points_df = pd.DataFrame(data = dataSet, columns = ['country_name','points'])
print('\n',olympic_points_df)