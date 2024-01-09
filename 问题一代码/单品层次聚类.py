import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import LabelEncoder

file_path = r"C:\Users\12426\Desktop\7月1日一小时.xlsx"
df = pd.read_excel(file_path)
# 将时间列转换为字符串，然后合并为datetime对象，最后提取时间
df['扫码销售时间'] = pd.to_datetime(df['扫码销售时间'].astype(str)).dt.time

# 对类别变量进行编码
label_encoder = LabelEncoder()
df['单品编码'] = label_encoder.fit_transform(df['单品名称'])

# 获取编码和单品名称的对应关系
label_mapping = dict(zip(df['单品编码'], df['单品名称']))
print(label_mapping)

# 提取需要聚类的数据
data_for_clustering = df[['扫码销售时间', '单品编码']]

# 以扫码销售时间为索引进行层次聚类
linkage_matrix = linkage(data_for_clustering.set_index('扫码销售时间'), method='ward')

# 画出树状图
plt.figure(figsize=(15, 8))
dendrogram(linkage_matrix, labels=data_for_clustering['单品编码'].tolist(), leaf_rotation=90)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Single Items')
plt.ylabel('Distance')
plt.show()
