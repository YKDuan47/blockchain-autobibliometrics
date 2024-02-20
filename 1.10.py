import pandas as pd
import numpy as np
df = pd.read_csv('国家共现矩阵.csv')
arr = df.to_numpy()
np.fill_diagonal(arr, 0)
df = pd.DataFrame(arr)
df.to_csv('国家共现矩阵1.csv', index=False)