import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = [
    "All",
    "Job\u2468",
    "Job\u246C",
    "Job\u246D",
    "Job\u246F",
]
athena = np.array([20.2, 100, 55.5, 50.4])
default = np.array([12.3, 10.2, 58.2, 25.3])
quiver = np.array([6.5, 100, 50.1, 15.2])
fluid = np.array([10.1, 65.3, 66.2, 43.3])

# 计算各方法的均值
default_mean = np.mean(default)
quiver_mean = np.mean(quiver)
fluid_mean = np.mean(fluid)
athena_mean = np.mean(athena)

# 将均值作为第一项加入
default = np.insert(default, 0, default_mean)
quiver = np.insert(quiver, 0, quiver_mean)
fluid = np.insert(fluid, 0, fluid_mean)
athena = np.insert(athena, 0, athena_mean)

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
ax.bar(index - 1.5 * bar_width, athena, bar_width, label='Athena', color=colors[0], hatch=hatches[0], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index - 0.5 * bar_width, default, bar_width, label='JuiceFS', color=colors[1], hatch=hatches[1], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + 0.5 * bar_width, quiver, bar_width, label='Quiver', color=colors[2], hatch=hatches[2], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + 1.5 * bar_width, fluid, bar_width, label='Fluid', color=colors[3], hatch=hatches[3], edgecolor='black', linewidth=1.2, zorder=3)

# 设置网格和边框
ax.grid(True, which='major', axis='both', zorder=0)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_edgecolor('black')
    spine.set_linewidth(1.0)

# 添加标签和刻度
ax.set_ylabel('CHR (%)', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=0)
yticks = [int(i) for i in ax.get_yticks() if i <= 100]
ax.set_ylim(0, 120)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

# 设置图例
handles, labels = ax.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.52, 1.03),
#            ncol=4, fontsize=legend_fontsize, frameon=False, handletextpad=0.5, columnspacing=1.0)

# 保存并显示图形
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()

# 提取 All 中的值
athena_all = athena_mean
default_all = default_mean
quiver_all = quiver_mean
fluid_all = fluid_mean

# 计算提升百分比
default_improvement = -(default_all - athena_all)
quiver_improvement = -(quiver_all - athena_all)
fluid_improvement = -(fluid_all - athena_all)

# 打印结果
print(f"Athena 相对于 Default 的提升: {default_improvement:.2f}%")
print(f"Athena 相对于 Quiver 的提升: {quiver_improvement:.2f}%")
print(f"Athena 相对于 Fluid 的提升: {fluid_improvement:.2f}%")

# 提取各 Job 的值（去掉 All 的均值）
athena_jobs = athena[1:]
default_jobs = default[1:]
quiver_jobs = quiver[1:]
fluid_jobs = fluid[1:]

# 计算每个 Job 上的提升百分比
default_improvements = -(default_jobs - athena_jobs)
quiver_improvements = -(quiver_jobs - athena_jobs)
fluid_improvements = -(fluid_jobs - athena_jobs)

# 打印结果
print("Athena 相对于 Default 的提升（各 Job）：", default_improvements)
print("Athena 相对于 Quiver 的提升（各 Job）：", quiver_improvements)
print("Athena 相对于 Fluid 的提升（各 Job）：", fluid_improvements)