import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

# 数据
large_file_times = [12.8, 9.9, 12.6]  # 无预取、块预取、文件预取
small_file_times = [240.1, 239.2, 52.2]  # 无预取、块预取、文件预取

# 归一化时间（以 No Prefetch 为基准）
large_file_times_normalized = [t / large_file_times[0] for t in large_file_times]
small_file_times_normalized = [t / small_file_times[0] for t in small_file_times]

# 参数设置
bar_width = 0.2  # 柱子宽度
x_large = np.array([0.45, 0.65])  # 大文件柱子位置（仅保留块预取、文件预取）
x_small = np.array([1.25, 1.45])  # 小文件柱子位置（仅保留块预取、文件预取）

colors = ['#e0543c', '#3989ba']  # 块预取、文件预取的颜色
plt.rcParams['axes.grid'] = False  # 禁用默认网格
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 开始绘图
fig, ax1 = plt.subplots(figsize=(6, 4))

# 左侧Y轴：绘制柱状图
ax1.bar(x_large[0], large_file_times_normalized[1], width=bar_width, color=colors[0], label='Block Prefetch', zorder=1)
ax1.bar(x_large[1], large_file_times_normalized[2], width=bar_width, color=colors[1], label='File Prefetch', zorder=1)

ax1.bar(x_small[0], small_file_times_normalized[1], width=bar_width, color=colors[0], zorder=1)  # Block Prefetch
ax1.bar(x_small[1], small_file_times_normalized[2], width=bar_width, color=colors[1], zorder=1)  # File Prefetch

# 设置左侧Y轴标签
ax1.set_ylabel('Normalized Time', color='black', fontsize=30)
ax1.set_xticks([0.55, 1.35])  # 设置两组簇的X轴位置
ax1.set_xticklabels(['Bookcorpus\nArrow', 'ImageNet\nTest'], fontsize=20)
ax1.set_xlim(0.1, 1.8)
ax1.set_ylim(0, max(max(large_file_times_normalized), max(small_file_times_normalized)) * 1.2)

# 修改刻度线
ax1.yaxis.grid(True, linestyle='--', alpha=0.5, zorder=0)  # 启用网格线
ax1.xaxis.grid(False)  # 禁用 x 轴网格线

# 修改 X 轴刻度字体
ax1.tick_params(axis='x', labelsize=24)  # 设置 X 轴刻度字体大小为 16
# 修改左 Y 轴刻度字体
ax1.tick_params(axis='y', labelsize=24)  # 设置左 Y 轴刻度字体大小为 16

# 图例
custom_legend = [
    Line2D([0], [0], color=colors[0], lw=10, label='B-P'),
    Line2D([0], [0], color=colors[1], lw=10, label='F-P'),
]

ax1.legend(
    handles=custom_legend,
    loc='lower center',  # 图例放置在底部居中
    bbox_to_anchor=(0.5, 1),  # 图例放在图表顶部，横向居中
    ncol=2,  # 图例分为 2 列
    frameon=True,  # 显示边框
    borderpad=0.5,  # 边框内边距
    columnspacing=2,  # 列间距
    handletextpad=0.8,  # 图例标记与文字的间距
    fontsize=20  # 图例字体大小
)

# 调整布局
plt.tight_layout()
plt.savefig('prefetch.pdf', facecolor='white', bbox_inches='tight')
plt.show()