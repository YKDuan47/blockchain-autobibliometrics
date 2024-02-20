from __future__ import print_function
import metaknowledge as mk
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
import gensim
from gensim import corpora, models
from stop_words import get_stop_words
from nltk.tokenize import RegexpTokenizer
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
import numpy as np

#抽取出需要分析的文本并转换为数组，保存为csv文件
folder_collec = mk.RecordCollection('data')
topic = folder_collec.forNLP('LDA_folder.csv', lower=True, removeNumbers=True)
document = topic['abstract']
docs = np.asarray(document)

#利用genism包进行LDA分析
#文本数据清洗
#分词
#去除停用词
#词向量化

#正则分词器，把所有的英文句子按单词断开
tokenizer = RegexpTokenizer(r'\w+')
#用于存放分词流
tokens = []
for l in document:
    #对一篇摘要进行分词并存为列表
    token = tokenizer.tokenize(l)
    tokens.append(token)
#tokens.append([tokenizer.tokenize(l) for l in document])

#去除停用词
#运用get_stop_word加载英文停用词列表
stopwords = get_stop_words('en')
#存放去除停用词后的词库
cleaned_tokens = []
for l in tokens:
    cleaned_tokens.append([i for i in l if not i  in stopwords])

#词句子向量化
dictionary = corpora.Dictionary(cleaned_tokens)
#https://blog.csdn.net/xuxiuning/article/details/47720337
#为语料库中的每个单词分配一个独一无二的ID，形成字典
array = np.asarray(cleaned_tokens)#转换为数组
corpus = [dictionary.doc2bow(word) for word in array]
#创建词袋模型，将每篇文档的摘要用向量来表示，该向量与原来文本中单词出现的顺序没有关系，而是词典中每个单词在文本中出现的频率
'''`
如存在一个语料库如下：
{"John": 1, "likes": 2,"to": 3, "watch": 4, "movies": 5,"also": 6, "football": 7, "games": 8,"Mary": 9, "too": 10}
一个句子向量如下：
  [1, 2, 1, 1, 1, 0, 0, 0, 1, 1]
  表示John出现了一次，likes出现了两次，to表示0次，watch表示0次~~~~~~~~~~~~~
'''
#投喂模型
ldamodel = gensim.models.ldamodel.LdaModel(corpus=corpus, num_topics=50, id2word=dictionary, passes=20)
#打印出前10个主题，以及每个主题中的前5个词语
print(ldamodel.print_topics(num_topics=10, num_words=5))
#存盘
dictionary.save('paper_abstracts.dict')
ldamodel.save('paper_abstracts_lda.model')

#可视化
vis_data = gensimvis.prepare(ldamodel, corpus, dictionary)
pyLDAvis.show(vis_data, open_browser=False)
