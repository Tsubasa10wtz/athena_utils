import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

import matplotlib.ticker as mtick
# 数据
large_file_times = [12.8, 9.9, 12.6]  # 无预取、块预取、文件预取
small_file_times = [240.1, 239.2, 52.2]  # 无预取、块预取、文件预取

# 归一化时间
large_file_times_normalized = [t / max(large_file_times) for t in large_file_times]
small_file_times_normalized = [t / max(small_file_times) for t in small_file_times]

# 缓存命中率数据
large_file_cache_hit = [0, 0.967, 0]  # 无预取、块预取、文件预取
small_file_cache_hit = [0, 0, 0.992]  # 块预取、文件预取、无预取

# 参数设置
bar_width = 0.2  # 柱子宽度
x_large = np.array([0.25, 0.45, 0.65])  # 大文件柱子位置
x_small = np.array([1.25, 1.45, 1.65])  # 小文件柱子位置（分组之间有间隔）

# plt.style.use("ggplot")  # 使用ggplot样式

colors= ['#e0543c', '#3989ba', '#998fd2']
plt.rcParams['axes.grid'] = False  # 禁用默认网格
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 开始绘图
fig, ax1 = plt.subplots(figsize=(8, 6))


# 左侧Y轴：绘制柱状图
ax1.bar(x_large[0], large_file_times_normalized[0], width=bar_width, color=colors[0], label='No Prefetch', zorder=1)
ax1.bar(x_large[1], large_file_times_normalized[1], width=bar_width, color=colors[1], label='Block Prefetch')
ax1.bar(x_large[2], large_file_times_normalized[2], width=bar_width, color=colors[2], label='File Prefetch')

ax1.bar(x_small[0], small_file_times_normalized[0], width=bar_width, color=colors[0])  # No Prefetch
ax1.bar(x_small[1], small_file_times_normalized[1], width=bar_width, color=colors[1])  # Block Prefetch
ax1.bar(x_small[2], small_file_times_normalized[2], width=bar_width, color=colors[2])  # File Prefetch

# 设置左侧Y轴标签
ax1.set_ylabel('Normalized JCT', color='black', fontsize=30)
ax1.set_xticks([0.45, 1.45])  # 设置两组簇的X轴位置
ax1.set_xticklabels(['Bookcorpus\nArrow', 'ImageNet\nTest'])
ax1.set_xlim(-0.2, 2.0)
ax1.set_ylim(0, 1.2)  # 缓存命中率范围0-1.2

# 右侧Y轴：缓存命中率
ax2 = ax1.twinx()
ax2.set_ylim(0, 1.2)  # 缓存命中率范围0-1.2

ax2.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))

# 修改所有刻度线的层级，并设置字体大小
ax1.tick_params(axis='both', which='both', direction='out', labelsize=26)
ax2.tick_params(axis='both', which='both', direction='out', labelsize=26)

ax1.yaxis.grid(True, zorder=0, linestyle='-', alpha=0.5)  # 只在 y 轴启用网格线
ax1.xaxis.grid(False)  # 禁用 x 轴网格线

# 绘制三角形标记缓存命中率
x_positions = list(x_large) + list(x_small)  # 所有柱子的位置
cache_hit_ratios = large_file_cache_hit + small_file_cache_hit  # 缓存命中率

for x, cache in zip(x_positions, cache_hit_ratios):
    ax2.scatter(x, cache, color='black', marker='^', facecolors='none', edgecolors='black', linewidths=1.5, s=100, clip_on=False, zorder=20)  # 在柱子顶部绘制三角形

# 图例
custom_legend = [
    Line2D([0], [0], color=colors[0], lw=10, label='No Prefetch'),
    Line2D([0], [0], color=colors[1], lw=10, label='Block Prefetch'),
    Line2D([0], [0], color=colors[2], lw=10, label='File Prefetch'),
    Line2D([0], [0], color='black', marker='^', markersize=10, label='Cache Hit Ratio', markerfacecolor='none', markeredgecolor='black', markeredgewidth=1.5, linestyle='None')
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
    fontsize=24  # 图例字体大小
)

# 调整布局
plt.tight_layout()
plt.savefig('prefetch_pro.pdf', facecolor='white', bbox_inches='tight')
plt.show()