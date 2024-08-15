import os
import re
from decimal import Decimal
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from scipy.stats import norm
import numpy as np

txt_path = 'tmp3.txt'

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

# 转换数据格式
data = np.array(differences_float).reshape(-1, 1)

# 使用高斯混合模型进行聚类
gmm = GaussianMixture(n_components=2, random_state=0)
gmm.fit(data)

# 获取聚类结果
labels = gmm.predict(data)
means = gmm.means_.flatten()
covariances = np.sqrt(gmm.covariances_).flatten()

plt.style.use("bmh")
plt.rcParams.update({'font.size': 16})

fig, ax = plt.subplots(figsize=(14, 8))

# 可视化
x = np.linspace(0, 4, 1000)  # 设置x轴的数据范围为0到4
for mean, std in zip(means, covariances):
    plt.plot(x, norm.pdf(x, mean, std), linewidth=2, label=f'Mean = {mean:.2f}, SD = {std:.2f}')

plt.title('Gaussian Mixture Modeling of Request Time Gaps')
plt.xlabel('Gap(s)')
plt.ylabel('Density')
plt.xlim(-1, 4.5)  # 设置x轴的显示范围为0到4

plt.grid(True, linestyle='--')  # 添加虚线网格线
plt.legend()

plt.show()
