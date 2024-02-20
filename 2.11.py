from pyecharts import ThemeRiver
import pandas as pd

data = pd.read_csv("./data/sale_amount.csv",encoding="gbk")
#print(data.head(5))
data["date"] = pd.to_datetime(data["date"],format='%Y-%m-%d') #转换时间类型并变为%Y-%m-%d
#print(data.head(5))
data.set_index('date',inplace=True)
#set_index设置索引（替换，真实覆盖）
#print(data)
ls=data.columns  #读取列表列头部
#print(data.columns)
dataone=[]
for d in range(data.shape[0]):
       for i in range(data.shape[1]):
              dataone.append([str(data.index[d]),data.iloc[d,i],data.columns[i]])
        #append结尾加[]内数据，间隔        #d行      #d行i列           #i列
print(dataone)
tr = ThemeRiver("主题河流图示意图")
tr.add(ls,dataone,
       is_label_show=True
       )
tr.render("tr.html")