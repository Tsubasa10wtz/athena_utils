import matplotlib.pyplot as plt
import numpy as np

# 数据
# categories = ['Overall', 'ImageNet', 'MITPlaces', 'OPT Loading', 'AudioMNIST', 'FashionProduct', 'AirQuality', 'ICOADS']
categories = ['All', 'Job\u2460', 'Job\u2461', 'Job\u2462', 'Job\u2463', 'Job\u2465', 'Job\u2467', 'Job\u246A',  ]
athena = np.array([95.2, 94.1, 65, 99, 77.3, 96.2, 97.1,  ])
no = np.array([0, 0, 0, 0, 0, 0, 0])
stride = np.array([0, 0, 52, 0, 74.3, 16.1, 0,  ])
juicefs = np.array([0, 0, 52, 0, 78.1, 16.1, 0,  ])
context = np.array([0, 0, 0, 0, 0, 0, 0])  # 添加context数据

# 计算各方法的均值
no_mean = np.mean(no)
stride_mean = np.mean(stride)
juicefs_mean = np.mean(juicefs)
context_mean = np.mean(context)  # 计算context均值
athena_mean = np.mean(athena)

# 打印juicefs和athena的均值
print(juicefs_mean)
print(athena_mean)

# 将均值作为第一项加入
no = np.insert(no, 0, no_mean)
stride = np.insert(stride, 0, stride_mean)
juicefs = np.insert(juicefs, 0, juicefs_mean)
context = np.insert(context, 0, context_mean)  # 插入context均值
athena = np.insert(athena, 0, athena_mean)

bar_width = 0.1  # 调整条形宽度，增加一个条形
index = np.arange(len(categories))  # 分类标签位置

fontsize = 28
legend_fontsize = 19
bar_width = 0.1  # 调整条形宽度以适应更多条形
index = np.arange(len(categories))  # 分类标签位置
figsize = (12, 4)

plt.style.use("ggplot")
plt.rcParams['font.family'] = 'Arial Unicode MS'
fig, ax = plt.subplots(figsize=figsize)  # 调整图表宽度以适应新列


# 按照顺序绘制条形图，顺序：Athena, No-Prefetch, Stride, Juicefs, Context
bar1 = ax.bar(index - 2 * bar_width, athena, bar_width, label='Athena')
bar2 = ax.bar(index - bar_width, no, bar_width, label='No-Prefetch')
bar3 = ax.bar(index, stride, bar_width, label='Stride')
bar4 = ax.bar(index + bar_width, juicefs, bar_width, label='Juicefs')
bar5 = ax.bar(index + 2 * bar_width, context, bar_width, label='SFP')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('CHR (%)', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=0)  # 调整为25度以便更好地显示标签
yticks = [int(i) for i in ax.get_yticks() if i <= 100]
ax.set_ylim(0, 100)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

# 设置图例
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()
