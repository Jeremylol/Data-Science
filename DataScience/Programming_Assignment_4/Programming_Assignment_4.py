import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats

turnstile_master = pd.read_csv('turnstile_data_master_with_weather.csv')
#1
#dataframe of hourly Entries
turnstile_weather = pd.DataFrame(turnstile_master['ENTRIESn_hourly'])
#hourly entries when it doesn't rain
non_rainy_data = turnstile_master[turnstile_master['rain'] == 0]['ENTRIESn_hourly']
# hourly entries when it is raining
rainy_data = turnstile_master[turnstile_master['rain'] == 1]['ENTRIESn_hourly']
print(non_rainy_data)
plt.hist([non_rainy_data, rainy_data], bins=25, stacked=True, color=['r', 'b'], label=['No Rain', 'Rain'])
plt.title('Histogram of ENTRIESn_hourly')
plt.xlabel('ENTRIESn_hourly')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.show()

#2
with_rain = turnstile_master[turnstile_master['rain'] == 1]['ENTRIESn_hourly']
with_rain_mean = np.mean(with_rain)

without_rain = turnstile_master[turnstile_master['rain'] == 0]['ENTRIESn_hourly']
without_rain_mean = np.mean(without_rain)
print('Mean of entries with rain:',with_rain_mean,'\nMean of entries without rain:',without_rain_mean)
[U, p] = scipy.stats.mannwhitneyu(with_rain, without_rain)
print('Mann-Whitney U-statistic:',U,'\np-Value:',p)
print('With the p-value of:',p,'being so low, it shows that we can reject our null hypothesis and find that \nthe distribution of the entries '
                                'is statistically different with rainy and non rainy days.')

#3
features = turnstile_master[['rain','Hour','meantempi','precipi']]
values = turnstile_master['ENTRIESn_hourly']

# Normalized
features = (features - features.mean()) / features.std()
features['ones'] = np.ones(len(values))
# Convert features and values to numpy arrays
features_array = np.array(features)
values_array = np.array(values)

alpha = 0.05
num_iterations = 100

theta = np.zeros(len(features.columns))

# Perform gradient descent
cost_history = []
for i in range(num_iterations):
    predicted_value = np.dot(features_array, theta)
    theta = theta + alpha/len(values) * np.dot(values_array - predicted_value, features_array)

    # Compute the cost function given a set of features / values
    sum_of_square = np.square(np.dot(features_array, theta) - values_array).sum()
    cost = sum_of_square / (2 * len(values))

    cost_history.append(cost)

cost_history = pd.Series(cost_history)

# Predictions
predictions = np.dot(features_array, theta)
# R^2
sqdata_predictions = np.sum((values - predictions)**2)
mean = np.mean(values)
sqdata_mean = np.sum((values - mean)**2)

rSquared = 1 - sqdata_predictions / sqdata_mean

print('\nR^2 value:',rSquared)


