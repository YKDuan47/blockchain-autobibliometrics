import metaknowledge as mk

RC = mk.RecordCollection("data/")
print(RC)

G = RC.networkCoCitation(nodeType='journal')
print(len(G.nodes()))
mk.writeGraph(G, "Cocitation-Network-of-Journals")
#mk.contour.plotting.graphDensityContourPlot(G,iters=50, layout=None, layoutScaleFactor=1, overlay=False, nodeSize=10, axisSamples=100, blurringFactor=0.1, contours=15, graphType='coloured')

mk.proquest.proQuestTagToFunc(G)
