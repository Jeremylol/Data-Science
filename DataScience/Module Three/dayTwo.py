import pandas as pd
import numpy as np
import scipy as sp

#generate same random data from normal distribution
# sample 50 data points with mean = 0 and variance = 1
data1= np.random.normal(0,1,size = 50) #mean, sd, size
data2 = np.random.normal(2,1,size = 50)
print(data1)
print(data2)
#one sample t-test
# the null hypotesis is that the mean m of the sample is equale to the true mean u of the population
# hence m == u, 95% confidence
onesampleresult = sp.stats.ttest_1samp(data1,0) # m == u
print(onesampleresult)
# we have two independently sampled datasets with equale variance and interested to know if u1 and u2 are identical
twosample_result = sp.stats.ttest_ind(data1,data2,equale_var = False)
print(twosample_result)
'''
 if p-value < statistics, reject the null hypothesis
 perform a t-test on two sets of baseball data(left handed and right hadnded players)
null hypothesis: there is no difference between the two groups
with 95% confidence level, is there is no difference between the two groups, output true and the tuple returned by scipy.stats.ttest
Ex output  true,(9.9357022,0.00023)
csv fle baseball_stats.csv     playername|handedness(Left/right)|avg   
read the data file into a data frame, split the data into two dataframes  for the left and right handedness
perform welches twosample ttest 
results = ?
if resuts[1] <=0.05:
print('False',results) #rejects null hypothesis, there is a difference 
else: print('True',results)
'''
