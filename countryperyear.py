import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import metaknowledge as mk
import csv
from matplotlib.pyplot import MultipleLocator

df = pd.read_csv('output.csv')
countrys = df['RP']
year = df['PY']

i = 0
for country in countrys:
    RP_words = str(countrys[i]).split()
    country = RP_words[-1]
    country = country.rstrip('.')
    countrys[i] = country
    i += 1

df['RP'] = countrys
countryPerYear = [countrys,year]
result = pd.concat(countryPerYear, axis=1)
#result.to_csv('countryPerYear.csv')
top10Country = countrys.value_counts()[:10]
#top10Country.to_csv('top10Country.csv')

#二重索引尝试
#df_1 = pd.read_csv('countryPerYear.csv')
#test = df_1.groupby(by=['RP','PY']).mean()
#test.to_csv('test.csv')

df_1 = pd.read_csv('countryPerYear.csv')
test = df_1.pivot_table(index=['RP','PY'],values=['sum'],aggfunc={'sum':np.sum},fill_value=0)
test.to_excel('test.xlsx')
readtest = pd.read_excel('test.xlsx')
RP = readtest['RP']
readtop10country = pd.read_csv('top10Country.csv',index_col=0)
#top10 = readtop10country['Unnamed: 0']
print(readtop10country)


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus'] = False	
	
data = pd.read_csv('Top10CountryperYear.csv')

xdata = []
y1data = []
y2data = []
y3data = []
y4data = []
y5data = []
y6data = []
y7data = []
y8data = []
y9data = []
y10data = []
xdata = data.loc[:,'year']
y1data = data.loc[:,'China']
y2data = data.loc[:,'USA']
y3data = data.loc[:,'Korea']
y4data = data.loc[:,'India']
y5data = data.loc[:,'England']
y6data = data.loc[:,'Australia']
y7data = data.loc[:,'Italy']
y8data = data.loc[:,'Spain']
y9data = data.loc[:,'Canada']
y10data = data.loc[:,'Germany']
plt.xlabel('Year')
plt.ylabel('Number of publications')

plt.plot(xdata, y1data, marker='o', markersize=3)  # 绘制折线图，添加数据点，设置点的大小
plt.plot(xdata, y2data, marker='o', markersize=3)
plt.plot(xdata, y3data, marker='o', markersize=3)
plt.plot(xdata, y4data, marker='o', markersize=3)
plt.plot(xdata, y5data, marker='o', markersize=3)
plt.plot(xdata, y6data, marker='o', markersize=3)
plt.plot(xdata, y7data, marker='o', markersize=3)
plt.plot(xdata, y8data, marker='o', markersize=3)
plt.plot(xdata, y9data, marker='o', markersize=3)
plt.plot(xdata, y10data, marker='o', markersize=3)
#不添加数据

x_major_locator=MultipleLocator(2)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)

plt.legend(['China', 'USA', 'Korea', 'India', 'England', 'Australia', 'Italy', 'Spain', 'Canada', 'Germany'])
plt.show()