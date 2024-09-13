import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Overall', 'ImageNet', 'MITPlaces', 'OPT Loading', 'AudioMNIST', 'FashionProduct', 'AirQuality', 'ICOADS']
athena = np.array([100, 105, 61, 25, 20, 1.2, 9.7])
no = np.array([584, 379, 87, 36, 83, 2.7, 35.2])
stride = np.array([572, 375, 66, 36, 81, 1.8, 35.4])
juicefs = np.array([545, 361, 63, 33, 83, 1.16, 35.1])
context = np.array([586, 380, 86, 35, 82, 2.7, 36.2])  # 添加新的context数据

# 归一化计算
no_norm = no / athena
print(no_norm)
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
legend_fontsize = 19
bar_width = 0.1  # 调整条形宽度以适应更多条形
index = np.arange(len(categories))  # 分类标签位置
figsize = (12, 6)

plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=figsize)  # 调整图表宽度以适应新列

# 绘制条形图，按照athena, no, stride, juicefs, context顺序
ax.bar(index - 2 * bar_width, athena_norm, bar_width, label='Athena')
ax.bar(index - bar_width, no_norm, bar_width, label='No-Prefetch')
ax.bar(index, stride_norm, bar_width, label='Stride')
ax.bar(index + bar_width, juicefs_norm, bar_width, label='JuiceFS')
ax.bar(index + 2 * bar_width, context_norm, bar_width, label='Context')

# 添加标签、标题和自定义x轴刻度标签
ax.set_ylabel('Normalized JCT', fontsize=fontsize)
ax.set_xticks(index)
ax.set_xticklabels(categories, fontsize=fontsize, rotation=25)  # 调整为25度以便更好地显示标签

yticks = [float(f"{i:.1f}") for i in ax.get_yticks()]
ax.set_ylim(0, max(yticks))
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

# 将图例放置在顶部
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()
