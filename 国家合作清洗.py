import pandas as pd
data = pd.read_csv('new_file.csv')
data.isnull().sum()
data = data.dropna()
new_df = data.applymap(lambda x: x if ',' in str(x) else None).dropna(how='all', axis=0).dropna(how='all', axis=1)
new_df.to_csv('国家共现.csv', index=False)