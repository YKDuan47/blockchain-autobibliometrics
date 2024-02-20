# 绘制关键词共现矩阵
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


WXdata=pd.read_csv('LDA_folder.csv',encoding="gbk")
# 定义函数，该函数主要用来分解信息，content为待处理内容，separator为拆分节点
def list_split(content,separator):  #分解信息函数
    new_list=[]
    for i in range(len(content)):
        new_list.append(list(filter(None,content[i].split(separator)))) # 此处采用了Python内置对象filter过滤器,对，后的数据实施，前的执行操作
    return new_list


#keyword=list_split(WXdata['keywords'].dropna(axis=0,how='all').tolist(),';;')
keyword=list_split(WXdata['keywords'].dropna(axis=0,how='all').tolist(),'|')
keyword1=sum(keyword,[])
data_keyword=pd.DataFrame(keyword1)[0].value_counts()[0:30].index.tolist();data_keyword

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

df_co_word_matrix = pd.read_csv('关键词共现.csv')
coword_names = df_co_word_matrix.columns.values[1:]
array_co_word_matrix = df_co_word_matrix.values[:, 1:].astype(float)
graph_co_word_matrix = nx.from_numpy_array(array_co_word_matrix)
Matrix3 = graph_co_word_matrix
print(Matrix3)
#Matrix3=occurence(data_keyword,keyword)
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False
graph3=nx.from_pandas_adjacency(Matrix3)
#nx.draw(graph3,with_labels=True,node_color='yellow')
nx.draw(graph3,with_labels=True,node_size = 15, font_size = 5, node_color = '#77787B', edge_color = '#D4D5CE', alpha= .95)
#plt.savefig('关键词共现.png')
plt.show()
#Matrix3.to_csv('关键词共现.csv')
