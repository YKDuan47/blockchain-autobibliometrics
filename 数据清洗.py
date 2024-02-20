import pandas as pd
data = pd.read_csv('title_year_author_instation.csv')
data.isnull().sum()
data = data.dropna()
data.to_csv('data.csv')