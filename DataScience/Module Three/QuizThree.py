import pandas as pd
import scipy
import scipy.stats
master_file = pd.read_csv('Master.csv')

height_mean = master_file['height'].mean()
weight_mean = master_file['weight'].mean()

print(height_mean)
print(master_file['height'].head(25))
imputed_df = master_file['height'].fillna(height_mean)
print(imputed_df.mean())
print(imputed_df.head(25))

print(weight_mean)
print(master_file['weight'].head(25))
imputed_df1 = master_file['weight'].interpolate()
print(imputed_df1.mean())
print(imputed_df1.head(25))

print(weight_mean)
print(master_file['weight'].head(25))
polynomial_df1 = master_file['weight'].interpolate(method = 'polynomial', order = 2)
print(polynomial_df1.mean())
print(polynomial_df1.head(25))

baseball = pd.read_csv('baseball_stats.csv')
leftHand = baseball["avg"][baseball["handedness"] == "L"]
rightHand = baseball["avg"][baseball["handedness"] == "R"]

(t, pvalue) = scipy.stats.ttest_ind(leftHand, rightHand, equal_var=False)
print('\n')
if pvalue > 0.05:
    print(True, (t, pvalue))
else:
    print(False, (t, pvalue))