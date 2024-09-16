import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['All', "job\u2468", "job\u246C", "job\u246D", "job\u246E"]
athena = np.array([273, 290, 1741, 48 * 60])
lru = np.array([344, 352, 1741, 48 * 60])
fifo = np.array([347, 348, 1765, 48 * 60 + 43])
lhd = np.array([342, 357, 1755, 48 * 60 + 32])
uniform = np.array([274, 293, 2296, 49 * 60 + 36])
sieve = np.array([344, 345, 1734, 48 * 60 + 52])

# 计算均值
athena_mean = 1
lru_mean = np.mean(lru / athena)
fifo_mean = np.mean(fifo / athena)
lhd_mean = np.mean(lhd / athena)
uniform_mean = np.mean(uniform / athena)
sieve_mean = np.mean(sieve / athena)

# 归一化计算
lru_norm = lru / athena
fifo_norm = fifo / athena
lhd_norm = lhd / athena
uniform_norm = uniform / athena
sieve_norm = sieve / athena

# 插入总体均值到数组的首位
athena_norm = np.insert(np.ones(len(athena)), 0, athena_mean)
lru_norm = np.insert(lru_norm, 0, lru_mean)
fifo_norm = np.insert(fifo_norm, 0, fifo_mean)
lhd_norm = np.insert(lhd_norm, 0, lhd_mean)
uniform_norm = np.insert(uniform_norm, 0, uniform_mean)
sieve_norm = np.insert(sieve_norm, 0, sieve_mean)

#
colors = ['#e24a33', '#348abd', '#988ed5', '#777777', "#fbc15e", "#8eba41", "#ffb4b8"]
fontsize = 28
legend_fontsize = 19
bar_width = 0.1  # 调整条形宽度以适应更多条形
index = np.arange(len(categories))  # 分类标签位置
figsize = (12, 6)

plt.style.use("ggplot")
plt.rcParams['font.family'] = 'Arial Unicode MS'
fig, ax = plt.subplots(figsize=figsize)  # 调整图表宽度以适应新列

# 按照 Athena、LRU、FIFO、LHD、Uniform、SIEVE 顺序绘制条形图
bar1 = ax.bar(index - 2.5 * bar_width, athena_norm, bar_width, label='Athena', color=colors[0])  # Athena 作为基准
bar2 = ax.bar(index - 1.5 * bar_width, lru_norm, bar_width, label='LRU', color=colors[1])
bar3 = ax.bar(index - 0.5 * bar_width, fifo_norm, bar_width, label='FIFO', color=colors[2])
bar4 = ax.bar(index + 0.5 * bar_width, lhd_norm, bar_width, label='LHD', color=colors[3])
bar5 = ax.bar(index + 1.5 * bar_width, uniform_norm, bar_width, label='Uniform', color=colors[4])
bar6 = ax.bar(index + 2.5 * bar_width, sieve_norm, bar_width, label='SIEVE', color=colors[5])  # SIEVE 列

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Normalized JCT', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=15)  # 调整为45度以便更好地显示标签
yticks = [float(f"{i:.1f}") for i in ax.get_yticks()]
ax.set_ylim(0, max(yticks))
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()
