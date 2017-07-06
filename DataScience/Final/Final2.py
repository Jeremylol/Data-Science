import pandas as pd

csv_file = pd.read_csv('APData.csv')
df = pd.DataFrame(csv_file)
df = df.replace('NR',0)
print(df)
