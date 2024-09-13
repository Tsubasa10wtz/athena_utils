import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = [
    "Overall",
    "ImageNet",
    "MITPlaces",
    "Twitter",
    "TPC-DS",
]
athena = np.array([15.2, 100, 14.2, 15.1])
default = np.array([6.3, 23.2, 10.1, 6.2])
quiver = np.array([0, 100, 0, 30.4])
fluid = np.array([50.1, 55.2, 0, 24.6])

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
figsize = (12, 6)

plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=figsize)  # 调整图表宽度以适应新列

# 按照顺序绘制条形图：Athena, Default, Quiver, Fluid
ax.bar(index - 1.5 * bar_width, athena, bar_width, label='Athena')
ax.bar(index - 0.5 * bar_width, default, bar_width, label='JuiceFS')  # Default 第二个
ax.bar(index + 0.5 * bar_width, quiver, bar_width, label='Quiver')    # Quiver 第三个
ax.bar(index + 1.5 * bar_width, fluid, bar_width, label='Fluid')      # Fluid 第四个

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Cache Hit Ratio (%)', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=15)  # 调整标签角度以提高可读性
yticks = [int(i) for i in ax.get_yticks() if i <= 100]
ax.set_ylim(0, 100)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()
