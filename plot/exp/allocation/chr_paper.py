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
# athena = np.array([13.2, 89.4, 90.1, 90.2])
# default = np.array([6.3, 23.2, 78.2, 78.3])
# quiver = np.array([0, 89.3, 0, 91.3])
# fluid = np.array([2.1, 75.3, 86.2, 90.3])

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

bar_width = 0.1  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置

fontsize = 28
legend_fontsize = 22
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
fig, ax = plt.subplots(figsize=figsize)  # 调整图表宽度以适应新列


# 按照顺序绘制条形图：Athena, Default, Quiver, Fluid
ax.bar(index - 1.5 * bar_width, athena, bar_width, label='Athena')
ax.bar(index - 0.5 * bar_width, default, bar_width, label='JuiceFS')  # Default 第二个
ax.bar(index + 0.5 * bar_width, quiver, bar_width, label='Quiver')    # Quiver 第三个
ax.bar(index + 1.5 * bar_width, fluid, bar_width, label='Fluid')      # Fluid 第四个

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('CHR (%)', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=0)  # 调整标签角度以提高可读性
yticks = [int(i) for i in ax.get_yticks() if i <= 100]
ax.set_ylim(0, 120)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

handles, labels = ax.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
#            ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()

# 提取All中的值
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