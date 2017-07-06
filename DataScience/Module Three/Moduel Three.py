import pandas as pd
import numpy as np
import scipy

#reindexing to get missing data
'''
df = pd.DataFrame(np.random.rand(5,3), index = ['a', 'c', 'e', 'f', 'h'], columns= ['one','two','three'])
print(df)
df2 = df.reindex(['a','b','c','d','e','f','g','h'])
print('\n',df2)
print('\n', pd.isnull(df2['one'])) # detect missing values
print(df2['two'].notnull())
#replace missing values with some scalar
df2 = df2.fillna(0) # fille nan with 0
print(df2)
dff = pd.DataFrame(np.random.randn(10,3), columns=list('ABC'))
print (dff)
#fill diff with nan's
dff.iloc[3:5,0] = np.nan
dff.iloc[4:6,1] = np.nan
dff.iloc[5:8,2] = np.nan
print(dff)
dff = dff.fillna(dff.mean()) # gives mean of the individual columns
#print(dff) comment when using the next print
dff = dff.fillna(dff.mean()['B':'C'])
print(dff)
#linear interpolation
df3 = pd.DataFrame({'A':[1,2.1,np.nan, 4.7, 5.6,6.8],
                    'B':[0.25,np.nan,np.nan,4,12.2,14.4]})
print(df3)
df3 = df3.interpolate()
print(df3)
#polynomial interpolation
df4 = pd.DataFrame({'A':[1,2.1,np.nan, 4.7, 5.6,6.8],
                    'B':[0.25,np.nan,np.nan,4,12.2,14.4]})
print(df4)
#df4 = df4.interpolate(method = 'polynomial', order = 2)  #problems downloading scipy
#print(df4)
'''
#class assignment
