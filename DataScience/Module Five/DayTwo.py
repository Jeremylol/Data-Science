'''
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn import datasets


iris = datasets.load_iris()
x = iris.data

pca = decomposition.pca(n_components = 3) # 3 different groups
pca.fit(x)
x = pca.transform(x)     # to this point it does all the pca
print(pca.explained_variance_ratio_)
fig = plt.figure(1, figsize=(7,5))
ax = fig.add_subplot(111,projection = '3d')
ax.scatter(x[:,0],x[:,1],x[:,2])
plt.show()

from sklearn.cluster import AgglomerativeClustering
from sklearn import clusters, dataset

iris = dataset.load_iris()
X_iris = iris.data
Y_iris = iris.target

iris = AgglomerativeClustering(n_clusters = 3, linkage = 'ward').fit_predict(X_iris)   #'ward' -> 'complete'  'average'
print(iris)
print('prediction\n', iris)
print('actual\n', Y_iris)
'''
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import proj3d

np.random.seed(7411)
mu_vec1 = np.array([0,0,0])
mu_vec2 = np.array([1,1,1])
cov_mat = np.array([[1,0,0],[0,1,0],[0,0,1]])

group1 = np.random.multivariate_normal(mu_vec1, cov_mat,20).T
group2 = np.random.multivariate_normal(mu_vec2, cov_mat,20).T

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection = '3d')
plt.rcParams['legend.fontsize'] = 10
ax.plot(group1[0,:],group1[1,:],group1[2,:],markersize = 8, color = 'blue', alpha = 0.5, label = 'group1')
ax.plot(group2[0,:],group2[1,:],group2[2,:],markersize = 8, color = 'red', alpha = 0.5, label = 'group2')
plt.title('Data Samples For Group1 And Group2')
ax.legend(loc = 'upper right')
plt.show()

#merge grp1/grp2 into 3x40 matrix thenc ompute the mean vector of d-dimensions

all_samples = np.concatenate((group1,group2), axis = 1)
#compute the meanvector
mean_x = np.mean(all_samples[0,:])
mean_y = np.mean(all_samples[1,:])
mean_z = np.mean(all_samples[2,:])

mean_vector = np.array([[mean_x],[mean_y], [mean_z]])
#compute variance matrix
cov_mat = np.cov([all_samples[0,:], all_samples[1,:], all_samples[2,:]])
print('covariance matrix\n',cov_mat)
#eiganvectors and eiganvalues from the covariance matrix
eig_val, eig_vec = np.linalg.eig(cov_mat)
print('eiganvector\n', eig_vec)
print('eiganvalues\n', eig_val)

#make alit of (eliganvalue, eliganvector) tuples
eig_pairs = [(np.abs(eig_val[:i], eig_vec[:,i])) for i in range (len(eig_val))]
eig_pairs.sort(key = lambda x: x[0], reversed = True)
#combine the two eiganvectors with the heighest eiganvalues to construct 2d matrix
matrixw = np.hstack((eig_pairs[0][1].reshape(3,1),eig_pairs[1][1].reshape(3,1)))
print(matrixw)
#use the matrixw to transform all_samples
transformed = matrixw.T.dot(all_samples)
plt.plot(transformed[0,0:20], transformed[1,0:20],'o',markersize = 7, color = 'blue', alpha = .5, label = 'group1')
plt.plot(transformed[0,20:40], transformed[1,20:40],'o',markersize = 7, color = 'red', alpha = .5, label = 'group1')