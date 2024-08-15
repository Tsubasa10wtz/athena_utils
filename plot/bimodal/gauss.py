import os
import re
from decimal import Decimal
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from scipy.stats import norm
import numpy as np

txt_path = 'tmp.txt'

with open(txt_path, 'r') as file:
    data = file.readlines()

print(data[0])

# 提取时间戳
pattern = r': ([\d.]+) -'
timestamps = [Decimal(re.search(pattern, line).group(1)) for line in data]

print(timestamps[0])

# 计算相邻时间戳的差值
differences = [abs(timestamps[i+1] - timestamps[i]) for i in range(len(timestamps) - 1)]

differences_float = [float(diff) for diff in differences]

data = np.array(differences_float).reshape(-1, 1)


# 使用高斯混合模型进行聚类
gmm = GaussianMixture(n_components=2, random_state=0)
gmm.fit(data)

# 获取聚类结果
labels = gmm.predict(data)
means = gmm.means_.flatten()
covariances = np.sqrt(gmm.covariances_).flatten()

print("x:", (means[1] - means[0])/(covariances[0] + covariances[1]))
# 双峰检测
if abs(means[1] - means[0]) > 10 * (covariances[0] + covariances[1]):
    print("数据可能存在双峰分布")
else:
    print("数据可能是单峰分布")

# 打印结果
print("Means:", means)
print("Standard Deviations:", covariances)

# 可视化
plt.figure(figsize=(20, 6))  # 调整图像大小
counts, bin_edges, _ = plt.hist(differences_float, bins='auto', density=True, alpha=0.7, color='grey', edgecolor='black', label='Data Histogram')
x = np.linspace(min(differences_float), max(differences_float), 1000)
colors = ['red', 'blue']  # 为每个组分选择颜色
for mean, std, color in zip(means, covariances, colors):
    plt.plot(x, norm.pdf(x, mean, std), linewidth=2, color=color, label=f'Mean = {mean:.2f}, SD = {std:.2f}')
plt.title('GMM Clustering and Distribution', fontsize=16)
plt.xlabel('Difference', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)  # 添加图例
plt.grid(True, linestyle='--')  # 添加虚线网格线

# 保存图像为PDF
# plt.savefig('GMM_Clustering_and_Distribution.pdf', format='pdf')


plt.show()

# 计算每个柱子的宽度
# bin_widths = np.diff(bin_edges)
#
# # 计算面积
# total_area = np.sum(counts * bin_widths)
#
# print("Total area under the histogram:", total_area)