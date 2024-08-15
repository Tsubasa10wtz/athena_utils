import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 0.01, size=1000)  # 生成一些正态分布数据

# 使用自动bins
plt.figure(figsize=(10, 6))
plt.hist(data, bins='auto', density=True, alpha=0.6, color='skyblue', edgecolor='black')
plt.title('Histogram with Auto Bins')
plt.show()

# 使用固定数量的bins
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
plt.title('Histogram with 30 Bins')
plt.show()

# 使用固定宽度的bins
bin_width = 0.005  # 选择合适的宽度
bins = np.arange(min(data), max(data) + bin_width, bin_width)
plt.figure(figsize=(10, 6))
plt.hist(data, bins=bins, density=True, alpha=0.6, color='skyblue', edgecolor='black')
plt.title('Histogram with Fixed Width Bins')
plt.show()
