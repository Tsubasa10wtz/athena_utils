import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

# 数据
categories = [
    "All",
    "Job\u2468",
    "Job\u246C",
    "Job\u246D",
    "Job\u246F",
]
athena = np.array([190, 58, 2450, 2549])
default = np.array([198, 159, 2100, 2624])
quiver = np.array([210, 61, 2500, 3423])
fluid = np.array([192, 82, 1945, 2821])

# 计算均值
default_mean = np.mean(default / athena)
quiver_mean = np.mean(quiver / athena)
fluid_mean = np.mean(fluid / athena)
athena_mean = np.mean(athena / athena)

# 归一化计算
default_norm = default / athena
quiver_norm = quiver / athena
fluid_norm = fluid / athena
athena_norm = athena / athena

# 插入总体均值到数组的首位
default_norm = np.insert(default_norm, 0, default_mean)
quiver_norm = np.insert(quiver_norm, 0, quiver_mean)
fluid_norm = np.insert(fluid_norm, 0, fluid_mean)
athena_norm = np.insert(athena_norm, 0, athena_mean)

# 样式设置
colors = ['#e0543c', '#3989ba', '#998fd2', '#777777', '#fac369']
hatches = ['/', '\\', '', 'x', '.', '', '.', '*']
fontsize = 28
legend_fontsize = 24
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

fig, ax = plt.subplots(figsize=figsize)

# 绘制条形图
ax.bar(index - 1.5 * bar_width, athena_norm, bar_width, label='Athena', color=colors[0], hatch=hatches[0], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index - 0.5 * bar_width, default_norm, bar_width, label='JuiceFS', color=colors[1], hatch=hatches[1], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + 0.5 * bar_width, quiver_norm, bar_width, label='Quiver', color=colors[2], hatch=hatches[2], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + 1.5 * bar_width, fluid_norm, bar_width, label='Fluid', color=colors[3], hatch=hatches[3], edgecolor='black', linewidth=1.2, zorder=3)

# 设置网格和边框
ax.grid(True, which='major', axis='both', zorder=0)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor('black')
    spine.set_linewidth(1.0)

# 添加标签和刻度
ax.set_ylabel('Normalized JCT', fontsize=fontsize, labelpad=10)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize)
yticks = [float(f"{i:.1f}") for i in ax.get_yticks()]
ax.set_ylim(0, 3.2)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))


# 设置图例
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.52, 1.03),
           ncol=4, fontsize=legend_fontsize, frameon=False, handletextpad=0.5, columnspacing=1.0)

# 保存并显示图形
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()

# 提取 All 中的值
athena_all = athena_norm[0]
default_all = default_norm[0]
quiver_all = quiver_norm[0]
fluid_all = fluid_norm[0]

# 计算提升百分比
default_improvement = (default_all - athena_all) / default_all * 100
quiver_improvement = (quiver_all - athena_all) / quiver_all * 100
fluid_improvement = (fluid_all - athena_all) / fluid_all * 100

# 打印结果
print(f"Athena 相对于 JuiceFS 的提升: {default_improvement:.2f}%")
print(f"Athena 相对于 Quiver 的提升: {quiver_improvement:.2f}%")
print(f"Athena 相对于 Fluid 的提升: {fluid_improvement:.2f}%")

athena_jobs = athena_norm[1:]
default_jobs = default_norm[1:]
quiver_jobs = quiver_norm[1:]
fluid_jobs = fluid_norm[1:]

# 计算每个 Job 上的提升百分比
default_improvements = (default_jobs - athena_jobs) / default_jobs * 100
quiver_improvements = (quiver_jobs - athena_jobs) / quiver_jobs * 100
fluid_improvements = (fluid_jobs - athena_jobs) / fluid_jobs * 100

# 打印结果
print("Athena 相对于 JuiceFS 的提升（各 Job）：", default_improvements)
print("Athena 相对于 Quiver 的提升（各 Job）：", quiver_improvements)
print("Athena 相对于 Fluid 的提升（各 Job）：", fluid_improvements)