import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

# 数据
# categories = ['Overall', 'ImageNet', 'MITPlaces', 'OPT Loading', 'AudioMNIST', 'FashionProduct', 'AirQuality', 'ICOADS']
categories = ['All', 'Job\u2460', 'Job\u2461', 'Job\u2462', 'Job\u2463','Job\u2465', 'Job\u2467', 'Job\u246A',  ]
athena = np.array([25, 20, 1.2, 9.7, 61, 100, 105,  ])
no = np.array([36, 83, 2.7, 35.2, 87, 584, 379,  ])
stride = np.array([36, 81, 1.8, 35.4, 66, 572, 375,  ])
juicefs = np.array([33, 83, 1.16, 35.1, 63, 545, 361,  ])
context = np.array([35, 82, 2.7, 36.2, 86, 586, 380,  ])  # 添加新的context数据

# 归一化计算
no_norm = no / athena
# print(no_norm)
juicefs_norm = juicefs / athena
stride_norm = stride / athena
context_norm = context / athena  # 计算context的归一化值
athena_norm = athena / athena

# 计算均值
no_mean = np.mean(no_norm)
juicefs_mean = np.mean(juicefs_norm)
stride_mean = np.mean(stride_norm)
context_mean = np.mean(context_norm)  # context均值
athena_mean = np.mean(athena_norm)

# 插入总体均值到归一化数据的首位
juicefs_norm = np.insert(juicefs_norm, 0, juicefs_mean)
stride_norm = np.insert(stride_norm, 0, stride_mean)
context_norm = np.insert(context_norm, 0, context_mean)  # 插入context均值
athena_norm = np.insert(athena_norm, 0, athena_mean)
no_norm = np.insert(no_norm, 0, no_mean)  # 插入 no 的均值

bar_width = 0.1  # 调整条形宽度，增加一个条形
index = np.arange(len(categories))  # 分类标签位置

fontsize = 28
legend_fontsize = 24
bar_width = 0.12  # 调整条形宽度以适应更多条形
index = np.arange(len(categories))  # 分类标签位置
figsize = (12, 4) # paper size
# figsize = (20, 4)

# plt.style.use("ggplot")
colors = ['#e0543c', '#3989ba', '#998fd2', '#777777', '#fac369']
hatches = ['/', '\\', '', 'x', '.',  '', '.', '*']
plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.rcParams.update({
    'text.color': 'black',         # 所有文本颜色
    'axes.labelcolor': 'black',    # 坐标轴标签颜色
    'xtick.color': 'black',        # x 轴刻度颜色
    'ytick.color': 'black',        # y 轴刻度颜色
    'axes.titlecolor': 'black',    # 坐标轴标题颜色
    'legend.labelcolor': 'black',  # 图例标签字体颜色
    'axes.facecolor': 'white',     # 坐标轴背景色为白色
    'figure.facecolor': 'white',   # 整体图像背景色为白色
    'grid.color': 'gray',          # 网格线颜色
    'grid.linestyle': '--',        # 网格线样式
    'grid.alpha': 0.5              # 网格线透明度
})
fig, ax = plt.subplots(figsize=figsize)  # 调整图表宽度以适应新列

# 绘制条形图，按照athena, no, stride, juicefs, context顺序
ax.bar(index - 2 * bar_width, athena_norm, bar_width, label='Athena', color=colors[0], hatch=hatches[0], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index - bar_width, no_norm, bar_width, label='No-Prefetch', color=colors[1], hatch=hatches[1], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index, stride_norm, bar_width, label='Stride', color=colors[2], hatch=hatches[2], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + bar_width, juicefs_norm, bar_width, label='JuiceFS', color=colors[3], hatch=hatches[3], edgecolor='black', linewidth=1.2, zorder=3)
ax.bar(index + 2 * bar_width, context_norm, bar_width, label='SFP', color=colors[4], hatch=hatches[4], edgecolor='black', linewidth=1.2, zorder=3)

ax.grid(True, which='major', axis='both', zorder=0)  # 启用网格
for spine in ax.spines.values():
    spine.set_visible(True)  # 显示边框
    spine.set_edgecolor('black')  # 边框颜色为黑色
    spine.set_linewidth(1.0)  # 边框宽度

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Normalized JCT', fontsize=fontsize, labelpad=10)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=0)  # 调整为25度以便更好地显示标签

# plt.xticks([])

yticks = [float(f"{i:.1f}") for i in ax.get_yticks()]
ax.set_ylim(0, max(yticks))
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))  # 每隔0.5一格


# 将图例放置在顶部
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.52, 1.03),
           ncol=6, fontsize=legend_fontsize, frameon=False, handletextpad=0.5, columnspacing=1.0)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()

# 归一化后的 Athena 和 Uniform 在 'All' 类别下的值
athena_all = athena_norm[0]  # 归一化后的 Athena 在 'All' 类别下的值
juicefs_all = juicefs_norm[0]  # 归一化后的 Uniform 在 'All' 类别下的值
print(athena_all)
print(juicefs_all)

# 计算归一化相对提升
relative_improvement_all = (juicefs_all - athena_all) / juicefs_all * 100

print(f"在 'All' 类别下，Athena 相较于 juicefs 的归一化相对提升为: {relative_improvement_all:.2f}%")
