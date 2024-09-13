import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Overall', 'ImageNet', 'MITPlaces', "Twitter\nCluster035", "TPC-DS"]  # 添加 'Overall' 类别
athena = np.array([25.3, 20.1, 89.3, 93.7])
lru = np.array([3, 1.9, 89.3, 93.7])
fifo = np.array([3.3, 2, 93.7, 93.8])
uniform = np.array([25.3, 20.1, 18.4, 91.7])
lhd = np.array([3.2, 1.9, 93.7, 94])
sieve = np.array([3, 1.9, 93.6, 94.1])  # 示例SIEVE数据

# 计算各方法的均值并作为第一项加入
lru_mean = np.mean(lru)
fifo_mean = np.mean(fifo)
uniform_mean = np.mean(uniform)
lhd_mean = np.mean(lhd)
athena_mean = np.mean(athena)
sieve_mean = np.mean(sieve)

lru = np.insert(lru, 0, lru_mean)
fifo = np.insert(fifo, 0, fifo_mean)
uniform = np.insert(uniform, 0, uniform_mean)
lhd = np.insert(lhd, 0, lhd_mean)
athena = np.insert(athena, 0, athena_mean)
sieve = np.insert(sieve, 0, sieve_mean)

bar_width = 0.05  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置

plt.style.use("ggplot")
plt.rcParams.update({'font.size': 24})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))

# 按照 Athena、LRU、FIFO、LHD、Uniform、SIEVE 顺序绘制条形图
bar1 = ax.bar(index - 2.5 * bar_width, athena, bar_width, label='Athena')
bar2 = ax.bar(index - 1.5 * bar_width, lru, bar_width, label='LRU')
bar3 = ax.bar(index - 0.5 * bar_width, fifo, bar_width, label='FIFO')
bar4 = ax.bar(index + 0.5 * bar_width, lhd, bar_width, label='LHD')
bar5 = ax.bar(index + 1.5 * bar_width, uniform, bar_width, label='Uniform')
bar6 = ax.bar(index + 2.5 * bar_width, sieve, bar_width, label='SIEVE')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Cache Hit Ratio(%)', fontsize=30)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=20)  # 旋转45度以便更好地显示标签
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=6, fontsize=20)
ax.set_ylim(0, 120)
ax.set_yticks(np.arange(0, 101, 20))  # 设置 y 轴的刻度，每隔10一个刻度，最大到100


# 显示图形并保存为白色背景的图片
plt.tight_layout()
plt.savefig('chr.pdf', bbox_inches='tight')
plt.show()