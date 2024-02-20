import metaknowledge as mk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

RC = mk.RecordCollection('data')
dfrpys = pd.DataFrame(RC.rpys(1981,2022))
a = dfrpys.head()
dev_line_color = sns.xkcd_rgb["pale red"]
print(a)
with sns.axes_style('white'):
        plt.plot(dfrpys['year'],dfrpys['abs-deviation'], dev_line_color)
        plt.plot([1981,2021],[0,0],linewidth = 1,color = 'black' )
        sns.despine()#offset = 10,trim = True)
        plt.vlines(x=2018,ymin=0,ymax=16000,linestyles="dashed")
        plt.vlines(x=2009,ymin=0,ymax=-2000,linestyles="dashed")
        plt.vlines(x=2008,ymin=0,ymax=2100,linestyles="dashed")
plt.show()