import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.patches import Patch

# 数据
# rag_cache_hit = [0.635, 0.506]  # LRU，Uniform
rag_cache_hit = [0.781, 0.506]  # LRU，Uniform
train_cache_hit = [0.123, 0.471]  # LRU，Uniform

# 参数设置
bar_width = 0.2  # 柱子宽度
x_rag = np.array([0.45, 0.65])  # LRU 和 Uniform 的位置
x_train = np.array([1.25, 1.45])  # LRU 和 Uniform 的位置（训练阶段）

colors = ['#e0543c', '#3989ba']  # LRU 和 Uniform 的颜色
plt.rcParams['axes.grid'] = False  # 禁用默认网格
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 开始绘图
fig, ax = plt.subplots(figsize=(6, 4))

# 将轴设置为网格线在底层
ax.set_axisbelow(True)

# 绘制柱状图，并设置较高的 zorder
ax.bar(x_rag[0], rag_cache_hit[0], width=bar_width, color=colors[0], label='LRU', zorder=2, edgecolor='black', linewidth=1.2,)
ax.bar(x_rag[1], rag_cache_hit[1], width=bar_width, color=colors[1], label='Uniform', zorder=2, edgecolor='black', linewidth=1.2,)

ax.bar(x_train[0], train_cache_hit[0], width=bar_width, color=colors[0], zorder=2, edgecolor='black', linewidth=1.2,)
ax.bar(x_train[1], train_cache_hit[1], width=bar_width, color=colors[1], zorder=2, edgecolor='black', linewidth=1.2,)

# 设置Y轴标签
ax.set_ylabel('Cache Hit Ratio (%)', fontsize=30)
ax.set_ylim(0, 1.1)  # 缓存命中率范围 0-1
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=0, symbol=''))  # 百分比显示

# 设置X轴标签和刻度
ax.set_xticks([0.55, 1.35])  # 设置两个簇的位置
ax.set_xlim(0.1, 1.8)
ax.set_xticklabels(['TriviaQA\nRAG', 'ImageNet\nTraining'], fontsize=20)

# 修改 X 轴和 Y 轴刻度字体
ax.tick_params(axis='x', labelsize=24)  # 设置 X 轴刻度字体大小
ax.tick_params(axis='y', labelsize=24)  # 设置 Y 轴刻度字体大小

# 启用网格线，并设置较低的 zorder
ax.yaxis.grid(True, linestyle='--', alpha=0.5, zorder=0)  # 启用 Y 轴网格线
ax.xaxis.grid(False)  # 禁用 X 轴网格线

# 图例
custom_legend = [
    Patch(facecolor=colors[0], edgecolor='black', lw=1.2, label='LRU'),  # 添加边框
    Patch(facecolor=colors[1], edgecolor='black', lw=1.2, label='Uniform'),  # 添加边框
]

ax.legend(
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
plt.savefig('eviction.pdf', facecolor='white', bbox_inches='tight')
plt.show()