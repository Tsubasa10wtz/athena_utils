import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

# 1. 定义节点数量 (x 轴)
node_counts = [1, 10, 100, 1000, 10000, 100000, 1000000]

plt.rcParams['font.family'] = 'Arial Unicode MS'

# 2. 三组原始数据
performance_values =        [1,    1,   1.05,   1.3,   2.1, 2.15, 2.16]
compute_overhead_values =   [4.3,    12.1,  24.1,  38.0,   47.6, 55.1, 60.4]  # us
memory_overhead_values =    [0.00634 / 1024,  0.0572 / 1024,  0.642 / 1024,    6.7 / 1024,  73.2 / 1024, 667.1 / 1024, 6972.1 / 1024]  # GB

# 3. 相对于节点数=1时的提升
performance_rel       = [performance_values[0] / v      for v in performance_values]
# compute_overhead_rel  = [v / compute_overhead_values[0] for v in compute_overhead_values]
# memory_overhead_rel   = [v / memory_overhead_values[0]  for v in memory_overhead_values]

# 颜色和标记
colors = ['tab:red', 'tab:blue', 'tab:green']
markers = ['o', '^', 's']

# 创建子图
fig, axes = plt.subplots(3, 1, figsize=(12, 8.7), sharex=False)
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 第一图：Performance
axes[0].plot(node_counts, performance_rel, marker=markers[0], color=colors[0], label='Normalized JCT',linewidth=5,markersize=10)
axes[0].set_ylabel('Overall\nJCT', fontsize=44)
axes[0].set_ylim(0, 1.2)
axes[0].yaxis.set_major_locator(MultipleLocator(0.5))
axes[0].legend(fontsize=34, loc='best')
axes[0].tick_params(axis='y', labelsize=18)
# axes[0].grid(True, which='both', linestyle='--', alpha=0.7)

# 第二图：Computational Overhead
axes[1].plot(node_counts, compute_overhead_values, marker=markers[1], color=colors[1], label='Comp. per I/O',linewidth=5,markersize=10)
axes[1].set_ylabel('Time\n(μs)', fontsize=44)
# axes[1].set_yscale('log')
axes[1].set_ylim(0, 60 * 1.2)
# axes[1].legend(fontsize=34, loc='best')
axes[1].legend(fontsize=34, loc='lower right', bbox_to_anchor=(1, -0.1))
axes[1].tick_params(axis='y', labelsize=18)
# axes[1].grid(True, which='both', linestyle='--', alpha=0.7)

# 第三图：Memory Overhead
axes[2].plot(node_counts, memory_overhead_values, marker=markers[2], color=colors[2], label='Memory Usage',linewidth=5,markersize=10)
axes[2].set_ylabel('Memory\n(GB)', fontsize=44, labelpad=20)
axes[2].set_ylim(0, 6.9 * 1.2)
axes[2].set_yticks(range(0, 7, 3))  # 只显示到 100 的刻度
axes[2].set_xlabel('Number of Nodes', fontsize=44)
# axes[2].set_yscale('log')
axes[2].legend(fontsize=34, loc='best')
axes[2].tick_params(axis='y', labelsize=18)
# axes[2].grid(True, which='both', linestyle='--', alpha=0.7)

for i in range(3):
    axes[i].set_xscale('log')
    axes[i].set_xticks(node_counts)
    axes[i].set_xticklabels([
        r'$10^0$', r'$10^1$', r'$10^2$', r'$10^3$', r'$10^4$', r'$10^5$', r'$10^6$'
    ], fontsize=18)
    axes[i].tick_params(axis='x', labelsize=34)
    axes[i].tick_params(axis='y', labelsize=34)

# 调整布局
fig.tight_layout()
plt.savefig('overhead.pdf', facecolor='white', bbox_inches='tight')
plt.show()