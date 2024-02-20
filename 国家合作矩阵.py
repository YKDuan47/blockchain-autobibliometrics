# 绘制作者共现矩阵
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text

WXdata=pd.read_csv('国家共现.csv')
# 定义函数，该函数主要用来分解信息，content为待处理内容，separator为拆分节点
def list_split(content,separator):  #分解信息函数
    new_list=[]
    for i in range(len(content)):
        new_list.append(list(filter(None,content[i].split(separator)))) # 此处采用了Python内置对象filter过滤器,对，后的数据实施，前的执行操作
    return new_list

# 定义新的函数，用新的标识来替代目标信息中的某些内容
def list_replace(content,old,new): 
    return [content[i].replace(old,new) for i in range(len(content))]

country=list_replace(WXdata['Country'].dropna(axis=0,how='all').tolist(),',',';')
country1=list_split(country,';')
country2=sum(country1,[])
data_country=pd.DataFrame(country2)[0].value_counts()[:31].index.tolist();data_country

def occurence(data,document):  #生成共现矩阵
    empty1=[];empty2=[];empty3=[]
    for a in data:
        for b in data:
            count = 0
            for x in document:
                if  [a in i for i in x].count(True) >0 and [b in i for i in x].count(True) >0:
                        count += 1
            empty1.append(a);empty2.append(b);empty3.append(count)
    df=pd.DataFrame({'from':empty1,'to':empty2,'weight':empty3})
    G=nx.from_pandas_edgelist(df, 'from', 'to', 'weight')
    return(nx.to_pandas_adjacency(G, dtype=int))

Matrix1=occurence(data_country,country1);Matrix1
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False
graph1=nx.from_pandas_adjacency(Matrix1)
#nx.draw(graph1,with_labels=True,node_color='black')
nx.draw(graph1,with_labels=True,node_size = 15, font_size = 5, node_color = '#77787B', edge_color = '#D4D5CE', alpha= .95)
plt.show()
Matrix1.to_csv('国家共现矩阵.csv')