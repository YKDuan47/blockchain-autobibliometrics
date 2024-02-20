import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 用pandas.read_csv方法来读取csv文件中的数据，返回一个DataFrame对象
df = pd.read_excel("大于100的文献.xlsx")

# 用value_counts方法来对国家列进行计数，返回一个Series对象
year_count = df["PY"].value_counts()

#year_count.to_csv('大于100的文献年份.csv')
year_count1 = pd.read_csv('大于100的文献年份.csv')
x_data = list(year_count1['PY'])
y_data = list(year_count1['sum'])
# 用seaborn.lineplot方法来画折线图，设置x轴和y轴的标签和标题
sns.lineplot(x=x_data, y=y_data)
plt.xlabel("Year")
plt.ylabel("Publications")
plt.title("Publications by Year")

# 显示折线图
plt.show()