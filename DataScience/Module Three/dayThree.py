import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


x = np.random.normal(0,1,size = 5000)
plt.hist(x,normed = True, bins = 50)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Normal Distribution Histogram')
plt.show()

W,P = sp.stats.shapiro(x)
if P < 0.05:
    print('Reject: data is not normal')
else:
    print('Accept: data is normal')

n,p = 10, 0.3 #trials and probability of each trial
Z = np.random.binomial(n,p,5000)
W,P = sp.stats.shapiro(Z)
if P < 0.05:
    print('Reject: data is not normal')
else:
    print('Accept: data is normal')



