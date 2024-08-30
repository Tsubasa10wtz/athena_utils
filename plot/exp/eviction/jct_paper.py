import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Overall', 'resnet\nimagenet', 'resnet\nmitplaces', 'alexnet\nimagenet', 'alexnet\nmitplaces', "twitter\ncluster035"]
lru = np.array([295, 336, 293, 332, 2690])
uniform = np.array([181, 230, 176, 227, 2938])
fifo = np.array([281, 330, 276, 325, 2580])
lhd = np.array([295, 334, 280, 332, 2570])  # 添加LHD数据
athena = np.array([182, 223, 177, 221, 2600])

# 计算均值
lru_mean = 1  # LRU 归一化到自身总是 1
uniform_mean = np.mean(uniform / lru)
fifo_mean = np.mean(fifo / lru)
lhd_mean = np.mean(lhd / lru)  # 计算LHD均值
athena_mean = np.mean(athena / lru)

# 归一化计算
uniform_norm = uniform / lru
fifo_norm = fifo / lru
lhd_norm = lhd / lru  # 归一化LHD
athena_norm = athena / lru

# 插入总体均值到数组的首位
uniform_norm = np.insert(uniform_norm, 0, uniform_mean)
fifo_norm = np.insert(fifo_norm, 0, fifo_mean)
lhd_norm = np.insert(lhd_norm, 0, lhd_mean)  # 插入LHD均值
athena_norm = np.insert(athena_norm, 0, athena_mean)

bar_width = 0.1  # 调整条形宽度以适应更少的条形
index = np.arange(len(categories))  # 分类标签位置

plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 24})  # 设置字体大小

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制条形图
bar1 = ax.bar(index - 2 * bar_width, np.insert(np.ones(len(lru)), 0, lru_mean), bar_width, label='LRU', edgecolor='black')  # LRU作为基准
bar2 = ax.bar(index - bar_width, fifo_norm, bar_width, label='FIFO', edgecolor='black')
bar3 = ax.bar(index, lhd_norm, bar_width, label='LHD', edgecolor='black')  # 插入LHD
bar4 = ax.bar(index + bar_width, uniform_norm, bar_width, label='Uniform', edgecolor='black')
bar5 = ax.bar(index + 2 * bar_width, athena_norm, bar_width, label='Athena', edgecolor='black')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('JCT', fontsize=30)
ax.set_xticks(index)
ax.set_xticklabels(categories)  # 调整为45度以便更好地显示标签

plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=5, fontsize=20)

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

# 显示图形并保存为白色背景的图片
plt.tight_layout()
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()
