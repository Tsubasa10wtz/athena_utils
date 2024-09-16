import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = [
    "Overall",
    "job\u2468",
    "job\u246C",
    "job\u246D",
    "job\u246E",
]
athena = np.array([172, 58, 1918, 2549])
default = np.array([198, 159, 2100, 2563])
quiver = np.array([210, 61, 3201, 2561])
fluid = np.array([192, 105, 2045, 2621])

# 计算均值
default_mean = np.mean(default / athena)  # default 归一化到自身总是 1
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

bar_width = 0.1  # 条形宽度
index = np.arange(len(categories))  # 分类标签位置

fontsize = 28
legend_fontsize = 22
figsize = (12, 6)

plt.style.use("ggplot")
plt.rcParams['font.family'] = 'Arial Unicode MS'
fig, ax = plt.subplots(figsize=figsize)  # 调整图表宽度以适应新列

# 按照顺序绘制条形图：Athena, JuiceFS, Quiver, Fluid
bar1 = ax.bar(index - 1.5 * bar_width, athena_norm, bar_width, label='Athena')
bar2 = ax.bar(index - 0.5 * bar_width, default_norm, bar_width, label='JuiceFS')  # JuiceFS 现在放在第二个位置
bar3 = ax.bar(index + 0.5 * bar_width, quiver_norm, bar_width, label='Quiver')
bar4 = ax.bar(index + 1.5 * bar_width, fluid_norm, bar_width, label='Fluid')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Normalized JCT', fontsize=fontsize)
# ax.set_title('JCT Of Different Space Management Solutions')
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=15)  # 调整为15度以便更好地显示标签
yticks = [float(f"{i:.1f}") for i in ax.get_yticks()]
ax.set_ylim(0, max(yticks))
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

# 设置图例
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()
