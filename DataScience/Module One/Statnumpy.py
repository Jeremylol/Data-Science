import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#numpy does calculations with lists/arrays
numbers = [1,2,3,4,5,6,7]

print (np.mean(numbers))
print (np.median(numbers))
print (np.std(numbers))

#pandas  which has rich data structures and makes computation fast and easy
series1 = pd.Series(['alan', 'Grant', 'TN', 45, -17 ])
print(series1)
series2 = pd.Series(['Dave','Lewis','Ky', 39, -9], index = ['FirstName', 'LastName','State', 'Age', 'Demerits'])
print (series2)

#Can use index to select specific item
print (series2['State'])

cuteness = pd.Series([1,2,3,4,5], index = ['bug', 'fish', 'pig', 'puppy', 'kitten'])
print(cuteness > 3)
print(" ")
print(cuteness[cuteness > 3])

# think of a data frame as something with rows & comulms similar to a spreadsheet or R's data.frame
data = {'year':[2010, 2011, 2012, 2012,2010],
        'team':['warriors','warriors','cavaliers','warriors','warriors'],
        'wins':[11, 8, 10, 15, 11],
        'losses':[5,4,3,2,1]
        }#data
basketball = pd.DataFrame(data)
print(basketball)

#more Pandas dataFrame
d = {'one':pd.Series([1,2,3], index = ['a','b','c']),
     'two':pd.Series([1,2,3,4], index = ['a','b','c','d'])}
df = pd.DataFrame(d)
print (df)

#functions apply, map, and applymap
print (df.apply(np.mean)) # perform the function on the vector that is every single column
#go through column one and evaluate wheather or not the value is greather than or equale to 1
print(df['one'].map(lambda x: x>1)) # map does one column of your choice
print(df.applymap(lambda x: x>1)) # applymap does all columns
# Numpy.dot allows you to do dot product
a = [1,2,3,4,5]
b = [6,7,8,9,10]
print (np.dot(a,b))
m1 = [1,2]
m2 = ([2,3,4],[5,6,7]) # first list is the first row
print(np.dot(m1,m2))
#inital set of baby names and births *matplotlibs*
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))
print(BabyDataSet)
#Create a DataFrame
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df)
#export data frame to a csv file
df.to_csv('births1880.csv', index = False, header = True)
#check for the file in current folder
Location = r'births1880.csv' # prefix the string with character r to escape the whole string #provide complete path
ndf = pd.DataFrame(pd.read_csv(Location))
print('\n')
print(ndf)
print(ndf.dtypes) # data types
print(ndf.describe()) # basic stats of the data
#find the most popular name, sort and pick the top values
Sorted = df.sort_values(['Births'],ascending= True)
print(Sorted.head(1))
print('\n')
print(df['Births'].max()) # gives just the number
MaxName = df['Names'][df['Births'] == df['Births'].max()].values # just gives max name
print(MaxName)
#df['Births'].plot()  #commented out to now have to bother with when running other functions
#plt.show()  #commented out to now have to bother with when running other functions

# inclass assignment
Location1 = r'C:\Users\Jeremy\Documents\CS\Data Science\Module 1\employee.csv'
edf = pd.DataFrame(pd.read_csv(Location1))
edf['Annual_Salary'] = edf['Annual_Salary'].replace('[\$,]',"", regex = True).astype(float)
print(edf['Annual_Salary'].max())

