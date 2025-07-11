import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

# 数据
categories = ['All', "Job\u2468", "Job\u246C", "Job\u246D", "Job\u246E"]
athena = np.array([7*60+22, 6*60+24, 1741, 9 * 60 + 12])
lru = np.array([11*60+2, 10*60+22, 1741, 9 * 60 + 11])
fifo = np.array([11*60+15, 10*60+24, 1765, 10 * 60 + 43])
arc = np.array([11*60+40, 10*60+30, 1755, 9 * 60 + 32])
uniform = np.array([7*60+24, 6*60+24, 2296, 38 * 60 + 51])
sieve = np.array([11*60, 10*60+30, 1734, 9 * 60])

# 计算均值
athena_mean = 1
lru_mean = np.mean(lru / athena)
fifo_mean = np.mean(fifo / athena)
arc_mean = np.mean(arc / athena)
uniform_mean = np.mean(uniform / athena)
sieve_mean = np.mean(sieve / athena)

# 归一化计算
lru_norm = lru / athena
fifo_norm = fifo / athena
arc_norm = arc / athena
uniform_norm = uniform / athena
sieve_norm = sieve / athena

# 插入总体均值到数组的首位
athena_norm = np.insert(np.ones(len(athena)), 0, athena_mean)
lru_norm = np.insert(lru_norm, 0, lru_mean)
fifo_norm = np.insert(fifo_norm, 0, fifo_mean)
arc_norm = np.insert(arc_norm, 0, arc_mean)
uniform_norm = np.insert(uniform_norm, 0, uniform_mean)
sieve_norm = np.insert(sieve_norm, 0, sieve_mean)

#
colors = ['#e24a33', '#348abd', '#988ed5', '#777777', "#fbc15e", "#8eba41", "#ffb4b8"]
fontsize = 28
legend_fontsize = 19
bar_width = 0.1  # 调整条形宽度以适应更多条形
index = np.arange(len(categories))  # 分类标签位置
figsize = (12, 4)

plt.style.use("ggplot")
plt.rcParams['font.family'] = 'Arial Unicode MS'
fig, ax = plt.subplots(figsize=figsize)  # 调整图表宽度以适应新列

# 按照 Athena、LRU、FIFO、arc、Uniform、SIEVE 顺序绘制条形图
bar1 = ax.bar(index - 2.5 * bar_width, athena_norm, bar_width, label='Athena', color=colors[0])  # Athena 作为基准
bar2 = ax.bar(index - 1.5 * bar_width, lru_norm, bar_width, label='LRU', color=colors[1])
bar3 = ax.bar(index - 0.5 * bar_width, fifo_norm, bar_width, label='FIFO', color=colors[2])
bar4 = ax.bar(index + 0.5 * bar_width, arc_norm, bar_width, label='ARC', color=colors[3])
bar5 = ax.bar(index + 1.5 * bar_width, uniform_norm, bar_width, label='Uniform', color=colors[4])
bar6 = ax.bar(index + 2.5 * bar_width, sieve_norm, bar_width, label='SIEVE', color=colors[5])  # SIEVE 列

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Normalized JCT', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=0)  # 调整为45度以便更好地显示标签
yticks = [float(f"{i:.1f}") for i in ax.get_yticks()]
ax.set_ylim(0, max(yticks))
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

ax.yaxis.set_major_locator(ticker.MultipleLocator(1))  # 每隔 1250 一格

handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
# plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()

# 归一化后的 Athena 和 Uniform 在 'All' 类别下的值
athena_all = athena_norm[0]  # 归一化后的 Athena 在 'All' 类别下的值
uniform_all = uniform_norm[0]  # 归一化后的 Uniform 在 'All' 类别下的值

# 计算归一化相对提升
relative_improvement_all = (uniform_all - athena_all) / uniform_all * 100

print(f"在 'All' 类别下，Athena 相较于 Uniform 的归一化相对提升为: {relative_improvement_all:.2f}%")

