import numpy as np
import pandas as pd

baseball = pd.read_csv('baseball_stats.csv')
features = baseball[['height','weight']].convert_objects(convert_numeric=True)
features = features.fillna(features.median())
features  = (features - features.mean())/features.std()
values = baseball['HR']
values = (values - values.mean())/values.std()
theta = np.random.normal(0.0, 1.0, size = 2)
#gradient descent setting
num_iterations = 100
alpha = .01

def compute_cost(features, values, theta):  # define an array of values as theta 0.0 1.0 normal distribution
    #compute cost for linear regression
    m = len(values) # of samples
    Sum_of_square_errors = np.square(features.apply(lambda x: np.dot(x, theta), axis = 1) - values).sum()  # J(0)
    cost = Sum_of_square_errors / (2 * m)
    return cost
# gradient descent
def gradient_descent(features,values,theta,alpha,num_iterations):
    m = len(values)
    cost_history = []
    for i in range(num_iterations):
     predicted_values = np.dot(features,theta)
     theta = theta - alpha / m * np.dot(predicted_values - values, features)
     cost = compute_cost(features,values,theta)
     cost_history.append(cost)
    return theta, pd.Series(cost_history)

print(gradient_descent(features,values,theta,alpha,num_iterations))