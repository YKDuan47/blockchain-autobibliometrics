import re # 正则表达式库
import collections
from matplotlib.cbook import flatten # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库
import pandas as pd

# 读取文件
fn = open('topKeywords.txt') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
object_list = []
remove_words = [u'|', u'of', u' ', u'and', u'things'] # 自定义去除词库

for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表

name = ['keywords']
test = pd.DataFrame(columns=name,data=object_list)
test.to_csv('keywords_fenci.csv')

df = pd.read_csv('keywords_fenci.csv')
content = df['keywords']
cut_word_list = list(map(lambda x: ''.join(x), content.tolist()))
content_str = ' '.join(cut_word_list).split()
word_fre = pd.Series(flatten(content_str)).value_counts()  # 统计词频
word_fre[:50]
keywords = word_fre[:50].index
keywords
matrix = np.zeros((len(keywords)+1)*(len(keywords)+1)).reshape(len(keywords)+1, len(keywords)+1).astype(str)
matrix[0][0] = np.NaN
matrix[1:, 0] = matrix[0, 1:] = keywords
matrix
kwdata = pd.DataFrame(data=matrix)
kwdata.to_csv('关键词共现矩阵.csv', index=False, header=None)

