import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

# 数据
# categories = ['All', "Job\u2468", "Job\u246C", "Job\u246D", "Job\u246E"]
# athena = np.array([7*60+22, 6*60+24, 10*60+11, 9 * 60 + 12])
# lru = np.array([11*60+2, 10*60+22, 10*60+20, 9 * 60 + 11])
# fifo = np.array([11*60+15, 10*60+24, 15*60+31, 12 * 60 + 43])
# arc = np.array([11*60+40, 10*60+30, 9*60+30, 8 * 60 + 32])
# uniform = np.array([7*60+24, 6*60+24, 39*60+11, 38 * 60 + 51])

# 新数据: train 1, train2, table1, table2, rag1, rag2
categories = ['All', "Job\u2468", "Job\u246C", "Job\u246D", "Job\u246F"]
athena = np.array([8.5*60+22, 7.5*60+24, 10*60+11, 9 * 60 + 12])
lru = np.array([11*60+2, 10*60+22, 10*60+20, 9 * 60 + 11])
fifo = np.array([11*60+15, 10*60+24, 15*60+31, 12 * 60 + 43])
arc = np.array([11*60+40, 10*60+30, 9*60+30, 8 * 60 + 32])
uniform = np.array([7*60+24, 6*60+24, 39*60+11, 20 * 60 + 51])

# 计算均值
athena_mean = 1
lru_mean = np.mean(lru / athena)
fifo_mean = np.mean(fifo / athena)
arc_mean = np.mean(arc / athena)
uniform_mean = np.mean(uniform / athena)

# 归一化计算
lru_norm = lru / athena
fifo_norm = fifo / athena
arc_norm = arc / athena
uniform_norm = uniform / athena

# 插入总体均值到数组的首位
athena_norm = np.insert(np.ones(len(athena)), 0, athena_mean)
lru_norm = np.insert(lru_norm, 0, lru_mean)
fifo_norm = np.insert(fifo_norm, 0, fifo_mean)
arc_norm = np.insert(arc_norm, 0, arc_mean)
uniform_norm = np.insert(uniform_norm, 0, uniform_mean)

# 颜色和样式设置
colors = ['#e24a33', '#348abd', '#988ed5', '#777777', "#fbc15e"]
fontsize = 28
legend_fontsize = 19
bar_width = 0.1  # 调整条形宽度
index = np.arange(len(categories))  # 分类标签位置
figsize = (12, 4)

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
plt.rcParams.update({
    'text.color': 'black',         # 所有文本颜色
    'axes.labelcolor': 'black',    # 坐标轴标签颜色
    'xtick.color': 'black',        # x 轴刻度颜色
    'ytick.color': 'black',        # y 轴刻度颜色
    'axes.titlecolor': 'black',    # 坐标轴标题颜色
    'legend.labelcolor': 'black',  # 图例标签字体颜色
})
fig, ax = plt.subplots(figsize=figsize)

# 绘制条形图
bar1 = ax.bar(index - 1.5 * bar_width, athena_norm, bar_width, label='Athena', color=colors[0])  # Athena 作为基准
bar2 = ax.bar(index - 0.5 * bar_width, lru_norm, bar_width, label='LRU', color=colors[1])
bar3 = ax.bar(index + 0.5 * bar_width, fifo_norm, bar_width, label='FIFO', color=colors[2])
bar4 = ax.bar(index + 1.5 * bar_width, arc_norm, bar_width, label='ARC', color=colors[3])
bar5 = ax.bar(index + 2.5 * bar_width, uniform_norm, bar_width, label='Uniform', color=colors[4])

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Normalized JCT', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=0)
yticks = [float(f"{i:.1f}") for i in ax.get_yticks()]
ax.set_ylim(0, max(yticks))
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))  # 每隔0.5一格


# 添加图例
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=5, fontsize=21, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
# plt.savefig('jct_no_sieve.pdf', facecolor='white', bbox_inches='tight')
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()

# 归一化后的 Athena 和 Uniform 在 'All' 类别下的值
athena_all = athena_norm[0]  # 归一化后的 Athena 在 'All' 类别下的值
arc_all = arc_norm[0]  # 归一化后的 Uniform 在 'All' 类别下的值

# 计算归一化相对提升
relative_improvement_all = (arc_all - athena_all) / arc_all * 100
print(athena_all)
print(arc_all)
print(f"在 'All' 类别下，Athena 相较于 ARC 的归一化相对提升为: {relative_improvement_all:.2f}%")