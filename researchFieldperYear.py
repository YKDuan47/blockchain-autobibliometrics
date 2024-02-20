import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import metaknowledge as mk
import csv

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus'] = False	
	
data = pd.read_csv('top10ResearchFieldperYear.csv')

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
y1data = data.loc[:,'Computer Science']
y2data = data.loc[:,'Engineering']
y3data = data.loc[:,'Business & Economics']
y4data = data.loc[:,'Chemistry']
y5data = data.loc[:,'Science & Technology - Other Topics']
y6data = data.loc[:,'Automation & Control Systems']
y7data = data.loc[:,'Telecommunications']
y8data = data.loc[:,'Energy & Fuels']
y9data = data.loc[:,'Mathematics']
y10data = data.loc[:,'Polymer Science']
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

plt.legend([
    'Computer Science',
    'Engineering',
    'Business & Economics',
    'Chemistry',
    'Science & Technology - Other Topics',
    'Automation & Control Systems',
    'Telecommunications',
    'Energy & Fuels',
    'Mathematics',
    'Polymer Science'
    ])
plt.show()


'Computer Science',
'Engineering',
'Business & Economics',
'Chemistry',
'Science & Technology - Other Topics',
'Automation & Control Systems',
'Telecommunications',
'Energy & Fuels',
'Mathematics',
'Polymer Science'
