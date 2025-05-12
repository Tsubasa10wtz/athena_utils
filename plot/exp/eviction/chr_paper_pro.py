import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
categories = ['All', "Job\u2468", "Job\u246C", "Job\u246D", "Job\u246F"]
# 数据
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

# 样式设置
colors = ['#e0543c', '#3989ba', '#998fd2', '#777777', '#fac369']  # 更新为之前的颜色
hatches = ['/', '\\', '', 'x', '.', '', '.', '*']  # 更新为之前的底纹样式
fontsize = 28
legend_fontsize = 19
bar_width = 0.12  # 调整条形宽度
index = np.arange(len(categories))  # 分类标签位置
figsize = (12, 4)

plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.rcParams.update({
    'text.color': 'black',
    'axes.labelcolor': 'black',
    'xtick.color': 'black',
    'ytick.color': 'black',
    'axes.titlecolor': 'black',
    'legend.labelcolor': 'black',
    'axes.facecolor': 'white',
    'figure.facecolor': 'white',
    'grid.color': 'gray',
    'grid.linestyle': '--',
    'grid.alpha': 0.5
})

categories = ['All', "Job\u2468", "Job\u246C", "Job\u246D", "Job\u246F"]

fig, ax = plt.subplots(figsize=figsize)

# 按照 Athena、LRU、FIFO、ARC、Uniform 顺序绘制条形图
ax.bar(index - 2 * bar_width, athena, bar_width, label='Athena', color=colors[0], hatch=hatches[0], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index - bar_width, lru, bar_width, label='LRU', color=colors[1], hatch=hatches[1], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index, fifo, bar_width, label='FIFO', color=colors[2], hatch=hatches[2], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + bar_width, arc, bar_width, label='ARC', color=colors[3], hatch=hatches[3], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + 2 * bar_width, uniform, bar_width, label='Uniform', color=colors[4], hatch=hatches[4], edgecolor='black', linewidth=1.2, zorder=3)

# 设置网格
ax.grid(True, which='major', axis='both', zorder=0)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor('black')
    spine.set_linewidth(1.0)

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('CHR (%)', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=0)
ax.set_ylim(0, 100)
yticks = [int(i) for i in ax.get_yticks() if i <= 100]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))  # 每20为一格

# 添加图例
handles, labels = ax.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=5, fontsize=legend_fontsize, frameon=False)

# 保存并显示图形
plt.tight_layout(rect=(0, 0, 1, 0.92))
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()

# 计算归一化相对提升
athena_all = athena_mean
arc_all = arc_mean

relative_improvement_all = (athena_all - arc_all)
print(athena_all)
print(arc_all)
print(f"在 'All' 类别下，Athena 相较于 ARC 的归一化相对提升为: {relative_improvement_all:.2f}%")