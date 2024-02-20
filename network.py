import metaknowledge as mk
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as ntx
import pandas as pd
import community


#合著网络
folder_collec = mk.RecordCollection('data')

RC1314 = folder_collec.yearSplit(2013, 2014)
#RC1314.writeCSV(r"F:\metaknow\example data\13141.csv")

coauth_net = folder_collec.networkCoAuthor()
print(mk.graphStats(coauth_net))
#minWeight=1
mk.dropEdges(coauth_net, minWeight= 1, dropSelfLoops= True)
print(mk.graphStats(coauth_net))
#minWeight=2
#mk.dropEdges(coauth_net, minWeight= 2, dropSelfLoops= True)
#print(mk.graphStats(coauth_net))
#minWeight=3
#mk.dropEdges(coauth_net, minWeight= 3, dropSelfLoops= True)
#print(mk.graphStats(coauth_net))
#minWeight=4
#mk.dropEdges(coauth_net, minWeight= 4, dropSelfLoops= True)
#print(mk.graphStats(coauth_net))
#minWeight=5
#mk.dropEdges(coauth_net, minWeight= 5, dropSelfLoops= True)
#print(mk.graphStats(coauth_net))
minWeight=20
mk.dropEdges(coauth_net, minWeight= 20, dropSelfLoops= True)
print(mk.graphStats(coauth_net))
#minWeight=7
#mk.dropEdges(coauth_net, minWeight= 7, dropSelfLoops= True)
#print(mk.graphStats(coauth_net))
#minWeight=10
#mk.dropEdges(coauth_net, minWeight= 10, dropSelfLoops= True)
#print(mk.graphStats(coauth_net))
#对网络节点进行筛选：去掉自循环的点；只保留最大网�?
connected_component_subgraphs = (coauth_net.subgraph(c) for c in ntx.connected_components(coauth_net))
giant_coauth = max(connected_component_subgraphs, key=len)
print(mk.graphStats(giant_coauth))
#计算网络指标
#degree度中心�?  eigenvector_centrality特征向量中心�? closeness_centrality中介中心�? betweenness_centrality接近中心�?
#deg = ntx.degree_centrality(coauth_net)
#eig = ntx.eigenvector_centrality(coauth_net)
#closeness = ntx.closeness_centrality(coauth_net)
#btw = ntx.betweenness_centrality(coauth_net)
# 转化为padas数据�?
#cent_df = pd.DataFrame.from_dict([deg, eig, closeness, btw])
#cent_df = pd.DataFrame.transpose(cent_df)
#cent_df.columns = ['degree', 'eigenvector', 'close_centra', 'betweeeness_centra']
#print(cent_df.sort_values('degree', ascending=False)[:10])

# 网络�?
#——整�?
#size = [1000 * eig[node] for node in coauth_net]
#ntx.draw_spring(coauth_net, node_size = size, with_labels = True, font_size = 5, node_color = '#FFFF00', edge_color = '#D4D5CE', alpha = .95)
#plt.savefig('network_coauthors.png')
#plt.show()

#整体中的最大网�?
#eig_giant = ntx.eigenvector_centrality(giant_coauth)
#size = [1000 * eig_giant[node] for node in giant_coauth]
#draw_sping(G,节点大小，是否显示节点标签，标签大小，节点颜色，边颜色，文本透明�?)
#ntx.draw_spring(giant_coauth, node_size = size, with_labels = True, font_size = 5, node_color = '#FFFF00', edge_color = '#D4D5CE', alpha = .95)
#plt.savefig('network_coauthors(min=6).png')
#plt.show()

#团体检�?
#partition = community.best_partition(coauth_net)
#modularity = community.modularity(partition, coauth_net)
#print('Modularity: ',modularity)
#colors = [partition[n] for n in coauth_net.nodes()]
#my_colors = plt.cm.Set1
#ntx.draw(coauth_net, node_color = colors, cmap = my_colors, edge_color = '#D4D5CE')
#plt.savefig('coauthors_communtity.png')
#plt.show() 

#同被引网�?
journal_cocition = folder_collec.networkCoCitation(coreOnly=True)
mk.dropEdges(journal_cocition, minWeight=50)
print(mk.graphStats(journal_cocition))
connected_component_subgraphs = (journal_cocition.subgraph(c) for c in ntx.connected_components(journal_cocition))
giant_journal = max(connected_component_subgraphs, key=len)
ntx.draw_spring(giant_journal, with_labels = True, node_size = 15, font_size = 5, node_color = '#77787B', edge_color = '#D4D5CE', alpha= .95)
#plt.savefig('network_journal_cocite.png')
plt.show()
