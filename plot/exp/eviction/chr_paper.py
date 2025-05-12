import matplotlib.pyplot as plt
import numpy as np

# 数据
# athena = np.array([47.3, 46.2, 73.1, 79.2])
# lru = np.array([14.1, 14.2, 73.0, 79.2])
# fifo = np.array([15.2, 16.1, 63.2, 67.1])
# uniform = np.array([47.1, 46.1, 11.9, 12.6])
# arc = np.array([15.3, 14.2, 78.6, 85.1])

# 新数据: finetuning, train 1, train2, table1, table2, rag1, rag2
athena = np.array([47.3, 46.2, 73.1, 79.2])
lru = np.array([14.1, 14.2, 73.0, 79.2])
fifo = np.array([15.2, 16.1, 63.2, 62.1])
uniform = np.array([47.1, 46.1, 11.9, 49.1])
arc = np.array([15.3, 14.2, 78.6, 85.1])

# 计算各方法的均值并作为第一项加入
lru_mean = np.mean(lru)
fifo_mean = np.mean(fifo)
uniform_mean = np.mean(uniform)
arc_mean = np.mean(arc)
athena_mean = np.mean(athena)

lru = np.insert(lru, 0, lru_mean)
fifo = np.insert(fifo, 0, fifo_mean)
uniform = np.insert(uniform, 0, uniform_mean)
arc = np.insert(arc, 0, arc_mean)
athena = np.insert(athena, 0, athena_mean)

# 图表设置
plt.style.use("ggplot")
plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.rcParams.update({
    'text.color': 'black',         # 所有文本颜色
    'axes.labelcolor': 'black',    # 坐标轴标签颜色
    'xtick.color': 'black',        # x 轴刻度颜色
    'ytick.color': 'black',        # y 轴刻度颜色
    'axes.titlecolor': 'black',    # 坐标轴标题颜色
    'legend.labelcolor': 'black',  # 图例标签字体颜色
})
categories = ['All', "Job\u2468", "Job\u246C", "Job\u246D", "Job\u246F"]
colors = ['#e24a33', '#348abd', '#988ed5', '#777777', "#fbc15e"]
fontsize = 28
legend_fontsize = 19
bar_width = 0.1  # 调整条形宽度
index = np.arange(len(categories))  # 分类标签位置
figsize = (12, 4)

fig, ax = plt.subplots(figsize=figsize)

# 按照 Athena、LRU、FIFO、ARC、Uniform 顺序绘制条形图
bar1 = ax.bar(index - 2 * bar_width, athena, bar_width, label='Athena')
bar2 = ax.bar(index - bar_width, lru, bar_width, label='LRU')
bar3 = ax.bar(index, fifo, bar_width, label='FIFO')
bar4 = ax.bar(index + bar_width, arc, bar_width, label='ARC')
bar5 = ax.bar(index + 2 * bar_width, uniform, bar_width, label='Uniform')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('CHR (%)', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=0)
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 20))  # 设置 y 轴的刻度
ax.set_yticklabels(ax.get_yticks(), fontsize=fontsize)

# 添加图例
handles, labels = ax.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
#            ncol=5, fontsize=legend_fontsize, frameon=False)

# 显示图形
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()

athena_all = athena_mean # 归一化后的 Athena 在 'All' 类别下的值
arc_all = arc_mean  # 归一化后的 Uniform 在 'All' 类别下的值

# 计算归一化相对提升
relative_improvement_all = (athena_all-arc_all)
print(athena_all)
print(arc_all)
print(f"在 'All' 类别下，Athena 相较于 ARC 的归一化相对提升为: {relative_improvement_all:.2f}%")