import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Overall', 'resnet\nimagenet', 'resnet\nmitplaces', 'alexnet\nimagenet', 'alexnet\nmitplaces', "ycsb"]
lru = np.array([295, 336, 293, 332, 2690])
uniform = np.array([181, 230, 176, 227, 2938])
fifo = np.array([281, 330, 276, 325, 2580])
athena = np.array([182, 223, 177, 221, 2600])

# 计算均值
lru_mean = 1  # LRU 归一化到自身总是 1
uniform_mean = np.mean(uniform / lru)
fifo_mean = np.mean(fifo / lru)
athena_mean = np.mean(athena / lru)

# 归一化计算
uniform_norm = uniform / lru
fifo_norm = fifo / lru
athena_norm = athena / lru

# 插入总体均值到数组的首位
uniform_norm = np.insert(uniform_norm, 0, uniform_mean)
fifo_norm = np.insert(fifo_norm, 0, fifo_mean)
athena_norm = np.insert(athena_norm, 0, athena_mean)

bar_width = 0.2  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 24})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制条形图
bar1 = ax.bar(index - 1.5 * bar_width, np.insert(np.ones(len(lru)), 0, lru_mean), bar_width, label='LRU')  # LRU作为基准
bar2 = ax.bar(index - 0.5 * bar_width, fifo_norm, bar_width, label='FIFO')
bar3 = ax.bar(index + 0.5 * bar_width, uniform_norm, bar_width, label='Uniform')
bar4 = ax.bar(index + 1.5 * bar_width, athena_norm, bar_width, label='Athena')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('JCT (Relative to LRU)')
ax.set_title('JCT Of Different Eviction Strategies')
ax.set_xticks(index)
ax.set_xticklabels(categories, rotation=45)  # 调整为45度以便更好地显示标签
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

# 显示图形
plt.tight_layout()
plt.show()