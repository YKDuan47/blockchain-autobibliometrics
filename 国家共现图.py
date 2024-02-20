import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pylab
import pandas as pd
df_co_word_matrix = pd.read_csv('task1_国家共现矩阵.csv')
coword_names = df_co_word_matrix.columns.values[1:]
print("There are ", len(coword_names), " words")
# 使用astype函数对数据类型进行转换，否则，下面画图的时候可能会报错
array_co_word_matrix = df_co_word_matrix.values[:, 1:].astype(float)
#看看有多少个词
word_num = len(array_co_word_matrix)
#graph_co_word_df = nx.from_pandas_adjacency(df_co_word_matrix)
graph_co_word_matrix = nx.from_numpy_array(array_co_word_matrix)
print(nx.info(graph_co_word_matrix))
#graph_co_word_matrix.edges(data=True)
coword_labels = nx.get_node_attributes(graph_co_word_matrix,'labels')
for idx, node in enumerate(graph_co_word_matrix.nodes()): 
    print("idx=", idx, "; node=", node)
    coword_labels[node] = coword_names[idx]
graph_co_word_matrix = nx.relabel_nodes(graph_co_word_matrix, coword_labels)
sorted(graph_co_word_matrix)
for idx, node in enumerate(graph_co_word_matrix.nodes()): 
    print("idx=", idx, "; node=", node)
pos = nx.spring_layout(graph_co_word_matrix)
plt.figure(1,figsize=(30,30)) 
#nx.draw(graph_co_word_matrix, pos, node_size=10, with_labels=True, font_size=22, font_color="red")
nx.draw(graph_co_word_matrix, pos, with_labels=True, font_size=25)
#nx.draw_networkx_labels(graph_co_word_matrix, pos, labels)
plt.show()

def diplay_graph_degree(G):
    seq_degree = sorted((d for n, d in G.degree()), reverse=True)
    dmax = max(seq_degree)
    
    fig = plt.figure("Degree of the count graph", figsize=(8, 8))
    # Create a gridspec for adding subplots of different sizes
    axgrid = fig.add_gridspec(5, 4)
    
    ax0 = fig.add_subplot(axgrid[0:3, :])
    Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    pos = nx.spring_layout(Gcc, seed=10396953)
    nx.draw_networkx_nodes(Gcc, pos, ax=ax0, node_size=20)
    nx.draw_networkx_edges(Gcc, pos, ax=ax0, alpha=0.4)
    ax0.set_title("Connected components of G")
    ax0.set_axis_off()
    
    ax1 = fig.add_subplot(axgrid[3:, :2])
    ax1.plot(seq_degree, "b-", marker="o")
    ax1.set_title("Degree Rank Plot")
    ax1.set_ylabel("Degree")
    ax1.set_xlabel("Rank")
    
    ax2 = fig.add_subplot(axgrid[3:, 2:])
    ax2.bar(*np.unique(seq_degree, return_counts=True))
    ax2.set_title("Degree histogram")
    ax2.set_xlabel("Degree")
    ax2.set_ylabel("# of Nodes")
    
    fig.tight_layout()
    plt.show()
sorted(graph_co_word_matrix.degree(), key=lambda x: x[1], reverse=True)
diplay_graph_degree(graph_co_word_matrix)