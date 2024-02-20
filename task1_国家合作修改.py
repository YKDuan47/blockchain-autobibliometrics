import pandas as pd

# 读取CSV文件
df = pd.read_csv('国家共现矩阵.csv', index_col=0)

# 将Hong Kong的值添加到China并删除Hong Kong列
df['China'] += df['Hong Kong']
df.drop('Hong Kong', axis=1, inplace=True)
df.drop('Hong Kong', axis=0, inplace=True)

# 将对角线的值改为0
for i in range(len(df.index)):
    df.iloc[i, i] = 0

# 将修改后的数据保存回CSV文件
df.to_csv('task1_国家共现矩阵.csv')
