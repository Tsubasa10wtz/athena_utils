import matplotlib.pyplot as plt
import numpy as np

categories = ['Overall', 'imagenet', 'mitplaces', "ycsb"]  # 添加 'Overall' 类别
lru = np.array([15.1, 20.4, 65.1])
fifo = np.array([20.6, 16.2, 65.1])
uniform = np.array([50.1, 49.3, 56.2])
athena = np.array([50.1, 49.3, 65.1])

# 计算各方法的均值
lru_mean = np.mean(lru)
fifo_mean = np.mean(fifo)
uniform_mean = np.mean(uniform)
athena_mean = np.mean(athena)

# 将均值作为第一项加入
lru = np.insert(lru, 0, lru_mean)
fifo = np.insert(fifo, 0, fifo_mean)
uniform = np.insert(uniform, 0, uniform_mean)
athena = np.insert(athena, 0, athena_mean)

bar_width = 0.2  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置，调整以包括 'Overall'

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 24})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制条形图
bar1 = ax.bar(index - 1.5 * bar_width, lru, bar_width, label='LRU')
bar2 = ax.bar(index - 0.5 * bar_width, fifo, bar_width, label='FIFO')
bar3 = ax.bar(index + 0.5 * bar_width, uniform, bar_width, label='Uniform')
bar4 = ax.bar(index + 1.5 * bar_width, athena, bar_width, label='Athena')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Cache Hit Ratio')
ax.set_title('Cache Hit Ratio of Different Eviction Strategies')
ax.set_xticks(index)
ax.set_xticklabels(categories, rotation=45)  # 调整为45度以便更好地显示标签
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

# 显示图形
plt.tight_layout()
plt.show()
