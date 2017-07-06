import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

np.set_printoptions(precision=5, suppress=True)  # suppress scientific notation
# generate 2 clusters of data a(size) = 100, b(size) = 50
np.random.seed(7411)  # change to a different prime if needed
a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100, ])
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50, ])
x = np.concatenate((a, b), )
print(x.shape)
plt.scatter(x[:, 0], x[:, 1])
plt.show()

z = linkage(x, 'single')  # try complete, average. word
print(z[:13])  # first thirteen iterations
# cophenetic correlation coefficient
# if ccc is closer to 1, the better the clustering preserves the original distances
c, coph_dists = cophenet(z, pdist(x)) # an array
print(c)

#generate dendrogram                                matrix z = idx1, idx2, distance, sample_count
plt.figure(figsize=(15,10))
plt.title('Hierarcgical Cluster Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distances')
dendrogram(z, leaf_rotation = 90,leaf_font_size= 8)
plt.show()

