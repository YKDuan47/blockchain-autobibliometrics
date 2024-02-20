import pandas as pd
data = pd.read_csv('output.csv')
data.isnull().sum()
data = data.dropna()
new_df = data.applymap(lambda x: x if ',' in str(x) else None).dropna(how='all', axis=0).dropna(how='all', axis=1)
new_df.to_csv('高被引文献年度0.csv', index=False)