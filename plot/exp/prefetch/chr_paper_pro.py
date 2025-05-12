import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['All', 'Job\u2460', 'Job\u2461', 'Job\u2462', 'Job\u2463', 'Job\u2465', 'Job\u2467', 'Job\u246A']
athena = np.array([95.2, 94.1, 65, 99, 77.3, 96.2, 97.1])
no = np.array([0, 0, 0, 0, 0, 0, 0])
stride = np.array([0, 0, 52, 0, 74.3, 16.1, 0])
juicefs = np.array([0, 0, 52, 0, 78.1, 16.1, 0])
context = np.array([0, 0, 0, 0, 0, 0, 0])  # 添加context数据

# 计算各方法的均值
no_mean = np.mean(no)
stride_mean = np.mean(stride)
juicefs_mean = np.mean(juicefs)
context_mean = np.mean(context)
athena_mean = np.mean(athena)

# 插入均值
no = np.insert(no, 0, no_mean)
stride = np.insert(stride, 0, stride_mean)
juicefs = np.insert(juicefs, 0, juicefs_mean)
context = np.insert(context, 0, context_mean)
athena = np.insert(athena, 0, athena_mean)

bar_width = 0.12  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置

# 样式设置
fontsize = 28
legend_fontsize = 19
figsize = (12, 4)
colors = ['#e0543c', '#3989ba', '#998fd2', '#777777', '#fac369']
hatches = ['/', '\\', '', 'x', '.',  '', '.', '*']

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

fig, ax = plt.subplots(figsize=figsize)

# 按顺序绘制条形图，设置颜色和底纹
ax.bar(index - 2 * bar_width, athena, bar_width, label='Athena', color=colors[0], hatch=hatches[0], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index - bar_width, no, bar_width, label='No-Prefetch', color=colors[1], hatch=hatches[1], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index, stride, bar_width, label='Stride', color=colors[2], hatch=hatches[2], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + bar_width, juicefs, bar_width, label='JuiceFS', color=colors[3], hatch=hatches[3], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + 2 * bar_width, context, bar_width, label='SFP', color=colors[4], hatch=hatches[4], edgecolor='black', linewidth=1.2, zorder=3)

# 设置网格和边框
ax.grid(True, which='major', axis='both', zorder=0)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor('black')
    spine.set_linewidth(1.0)

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('CHR (%)', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize)
yticks = [int(i) for i in ax.get_yticks() if i <= 100]
ax.set_ylim(0, 110)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

# 设置图例
handles, labels = ax.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.0),
#            ncol=5, fontsize=legend_fontsize, frameon=False)

# 保存和显示图形
plt.tight_layout(rect=(0, 0, 1, 0.92))
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()

# 计算Athena相对于JuiceFS的增加量
athena_all = athena[0]
juicefs_all = juicefs[0]
increase = athena_all - juicefs_all
print(f"Athena 相对于 Uniform 在 'All' 上的增加量: {increase:.2f}%")