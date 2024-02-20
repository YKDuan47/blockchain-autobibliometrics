import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import metaknowledge as mk
import csv

df = pd.read_csv('output.csv')
journals = df['J9']
year = df['PY']

df['J9'] = journals
journalPerYear = [journals,year]
result = pd.concat(journalPerYear, axis=1)
#result.to_csv('journalPerYear.csv')
top10journal = journals.value_counts()[:10]
#top10journal.to_csv('top10journal.csv')

#二重索引尝试
#df_1 = pd.read_csv('journalPerYear.csv')
#test = df_1.groupby(by=['J9','PY']).mean()
#test.to_csv('test.csv')

df_1 = pd.read_csv('journalPerYear.csv')
test = df_1.pivot_table(index=['J9','PY'],values=['sum'],aggfunc={'sum':np.sum},fill_value=0)
#test.to_excel('testJournal.xlsx')
readtest = pd.read_excel('testJournal.xlsx')
J9 = readtest['J9']
#readtop10journal = pd.read_csv('top10journal.csv',index_col=0)
#top10 = readtop10journal['Unnamed: 0']
#print(readtop10journal)

	
data = pd.read_csv('Top10JournalperYear.csv')

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
y1data = data.loc[:,'IEEE ACCESS']
y2data = data.loc[:,'IEEE INTERNET THINGS']
y3data = data.loc[:,'SENSORS-BASEL']
y4data = data.loc[:,'SUSTAINABILITY-BASEL']
y5data = data.loc[:,'APPL SCI-BASEL']
y6data = data.loc[:,'ELECTRONICS-SWITZ']
y7data = data.loc[:,'IEEE NETWORK']
y8data = data.loc[:,'FUTURE GENER COMP SY']
y9data = data.loc[:,'SECUR COMMUN NETW']
y10data = data.loc[:,'IEEE T IND INFORM']
plt.xlabel('Year')
plt.ylabel('Number of Publications')

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
my_x_ticks = np.arange(2013, 2022, 1)#原始数据有13个点，故此处为设置从0开始，间隔为1
plt.xticks(my_x_ticks, rotation = 45)

plt.legend([
    'IEEE ACCESS',
    'IEEE INTERNET THINGS',
    'SENSORS-BASEL',
    'SUSTAINABILITY-BASEL',
    'APPL SCI-BASEL',
    'ELECTRONICS-SWITZ',
    'IEEE NETWORK',
    'FUTURE GENER COMP SY',
    'SECUR COMMUN NETW',
    'IEEE T IND INFORM'
])
plt.show()