import matplotlib.pyplot as plt
import numpy as np

# 数据
# categories = ['All', "Job\u2468", "Job\u246C", "Job\u246D", "Job\u246E"]
athena = np.array([47.3, 29.1, 89.3, 93.7])
lru = np.array([14.1, 1.9, 89.3, 93.7])
fifo = np.array([15.2, 2, 93.7, 93.8])
uniform = np.array([47.1, 20.1, 18.4, 91.7])
arc = np.array([15.3, 1.9, 93.7, 94])
sieve = np.array([15.3, 1.9, 93.6, 94.1])  # 示例SIEVE数据

# 计算各方法的均值并作为第一项加入
lru_mean = np.mean(lru)
fifo_mean = np.mean(fifo)
uniform_mean = np.mean(uniform)
arc_mean = np.mean(arc)
athena_mean = np.mean(athena)
sieve_mean = np.mean(sieve)

lru = np.insert(lru, 0, lru_mean)
fifo = np.insert(fifo, 0, fifo_mean)
uniform = np.insert(uniform, 0, uniform_mean)
arc = np.insert(arc, 0, arc_mean)
athena = np.insert(athena, 0, athena_mean)
sieve = np.insert(sieve, 0, sieve_mean)


plt.style.use("ggplot")
plt.rcParams['font.family'] = 'Arial Unicode MS'
rotation = 15
categories = ['All', "Job\u2468", "Job\u246C", "Job\u246D", "Job\u246E"]
colors = ['#e24a33', '#348abd', '#988ed5', '#777777', "#fbc15e", "#8eba41", "#ffb4b8"]
fontsize = 28
legend_fontsize = 19
bar_width = 0.1  # 调整条形宽度以适应更多条形
index = np.arange(len(categories))  # 分类标签位置
figsize = (12, 4)

fig, ax = plt.subplots(figsize=figsize)

index = np.arange(len(categories))  # 分类标签位置
# 按照 Athena、LRU、FIFO、LHD、Uniform、SIEVE 顺序绘制条形图
bar1 = ax.bar(index - 2.5 * bar_width, athena, bar_width, label='Athena')
bar2 = ax.bar(index - 1.5 * bar_width, lru, bar_width, label='LRU')
bar3 = ax.bar(index - 0.5 * bar_width, fifo, bar_width, label='FIFO')
bar4 = ax.bar(index + 0.5 * bar_width, arc, bar_width, label='ARC')
bar5 = ax.bar(index + 1.5 * bar_width, uniform, bar_width, label='Uniform')
bar6 = ax.bar(index + 2.5 * bar_width, sieve, bar_width, label='SIEVE')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('CHR (%)', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=0)  # 旋转45度以便更好地显示标签
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 20))  # 设置 y 轴的刻度，每隔10一个刻度，最大到100
ax.set_yticks(ax.get_yticks())
ax.set_yticklabels(ax.get_yticks(), fontsize=fontsize)

handles, labels = ax.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
#            ncol=6, fontsize=legend_fontsize, frameon=False)


# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('chr.pdf', bbox_inches='tight')
plt.show()

athena_all = athena[0]
print(athena_all)
arc_all = arc[0]
print(lhd_all)
increase = athena_all - lhd_all
print(f"Athena 相对于 Uniform 在 'All' 上的增加量: {increase}%")