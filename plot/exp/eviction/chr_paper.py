import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Overall', 'imagenet', 'mitplaces', "twitter\ncluster035"]  # 添加 'Overall' 类别
lru = np.array([15.1, 20.4, 65.1])
fifo = np.array([20.6, 16.2, 65.1])
uniform = np.array([50.1, 49.3, 56.2])
lhd = np.array([21.5, 25.2, 67.3])  # 添加LHD数据
athena = np.array([50.1, 49.3, 65.1])

# 计算各方法的均值
lru_mean = np.mean(lru)
fifo_mean = np.mean(fifo)
uniform_mean = np.mean(uniform)
lhd_mean = np.mean(lhd)
athena_mean = np.mean(athena)

# 将均值作为第一项加入
lru = np.insert(lru, 0, lru_mean)
fifo = np.insert(fifo, 0, fifo_mean)
uniform = np.insert(uniform, 0, uniform_mean)
lhd = np.insert(lhd, 0, lhd_mean)  # 插入LHD均值
athena = np.insert(athena, 0, athena_mean)

bar_width = 0.05  # 调整条形宽度以适应更少的列
index = np.arange(len(categories))  # 分类标签位置，调整以包括 'Overall'

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 24})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制条形图
bar1 = ax.bar(index - 2 * bar_width, lru, bar_width, label='LRU', edgecolor='black')
bar2 = ax.bar(index - bar_width, fifo, bar_width, label='FIFO', edgecolor='black')
bar3 = ax.bar(index, lhd, bar_width, label='LHD', edgecolor='black')  # 插入LHD
bar4 = ax.bar(index + bar_width, uniform, bar_width, label='Uniform', edgecolor='black')
bar5 = ax.bar(index + 2 * bar_width, athena, bar_width, label='Athena', edgecolor='black')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Cache Hit Ratio', fontsize=30)
ax.set_xticks(index)
ax.set_xticklabels(categories)  # 调整为45度以便更好地显示标签
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5, fontsize=20)

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

# 显示图形并保存为白色背景的图片
plt.tight_layout()
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()
