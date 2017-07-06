import pandas as pd
import pandasql
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats


print('Question 1:')# Question 1
csv_file = pd.read_csv('APData.csv')
df = pd.DataFrame(csv_file)
df = df.replace('NR',0)
print(df)

print('Question 2:')# Question 2
question_one = df['2a']
mean1 = np.mean(question_one)
median1 = np.median(question_one)
std1 = np.std(question_one)
print('Question 1\'s mean:',mean1,' median:',median1,' Standard Deviation:',std1)
question_two = df['2b'].astype(int)
mean2 = np.mean(question_two)
median2 = np.median(question_two)
std2 = np.std(question_two)
print('Question 2\'s mean:',mean2,' median:',median2,' Standard Deviation:',std2)
question_three = df['2c'].astype(int)
mean3 = np.mean(question_three)
median3 = np.median(question_three)
std3 = np.std(question_three)
print('Question 3\'s mean:',mean3,' median:',median3,' Standard Deviation:',std3)
question_four = df['2d'].astype(int)
mean4 = np.mean(question_four)
median4 = np.median(question_four)
std4 = np.std(question_four)
print('Question 4\'s mean:',mean4,' median:',median4,' Standard Deviation:',std4,'\n')


# Question 3
print("Question 3:")
q = "SELECT Language, count(Language) FROM df GROUP BY Language"
sql_language = pandasql.sqldf(q.lower(),locals())
print(sql_language.max())
print(sql_language.min())
q2 = "SELECT * FROM df"
sql_language1 = pandasql.sqldf(q2.lower(),locals())
print('Question 2d')
print('Question 2a')
q3 = "SELECT ID FROM df WHERE '2d' < 2"
sql_language2 = (pandasql.sqldf(q3.lower(), locals()))
print(sql_language2)




# Question 4
print("\nQuestion 4:")
histogram_one = df['2c'].astype(int)
plt.hist(histogram_one, stacked=True, color = ['r'])
plt.title('Histogram of 2c')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

histogram_one = df['2d'].astype(int)
plt.hist(histogram_one, stacked=True, color = ['b'])
plt.title('Histogram of 2d')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
print('Yes, The data is normally distributed')

# Question 5
print("Question 5:")
data1 = df['2c'].astype(int)
onesampleresult = sp.stats.ttest_1samp(data1,0)
print('T-test for 2c:',onesampleresult)
data2 = df['2d'].astype(int)
twosample_result = sp.stats.ttest_1samp(data2,0)
print('T-test for 2d:',twosample_result)


#Question 6
print("Question 6:")
features = df[['2b','2c','2d']].astype(int)
values = df['2b'].astype(int)
print('Coefficients:\n',values)
# Normalized
features = (features - features.mean()) / features.std()
features['ones'] = np.ones(len(values))
# Convert features and values to numpy arrays
features_array = np.array(features)
values_array = np.array(values)

alpha = 0.05
num_iterations = 50

theta = np.zeros(len(features.columns))

# Perform gradient descent
cost_h = []
for i in range(num_iterations):
    predicted_value = np.dot(features_array, theta)
    theta = theta + alpha/len(values) * np.dot(values_array - predicted_value, features_array)

    # Compute the cost function given a set of features / values
    sum_of_square = np.square(np.dot(features_array, theta) - values_array).sum()
    cost = sum_of_square / (2 * len(values))

    cost_h.append(cost)

cost_h = pd.Series(cost_h)

# Predictions
predictions = np.dot(features_array, theta)
# R^2
sqdata_predictions = np.sum((values - predictions)**2)
mean = np.mean(values)
sqdata_mean = np.sum((values - mean)**2)

rSquared = 1 - sqdata_predictions / sqdata_mean
print('\nQuestion 7:')
print('R^2 value:',rSquared)
print('R^2 is very close to 1, making our model very effective')


# Question 8
print('\nQuestion 8:  CANNOT SEE RESULTS, Couldn\'t download sklearn')

df2 = datasets.load_files('APData.csv')
X_df2 = df2.data
Y_df2 = df2.target
K_means = cluster.KMeans(n_clusters = 5)
K_means.fit(X_df2)
print(K_means.labels_[::10])
print(df2[::10])

