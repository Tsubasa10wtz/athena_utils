import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

# 模拟参数
num_samples = 1300
num_epochs = 1

# 记录所有访问顺序
access_order = []

# 每个 epoch shuffle 后记录访问顺序
for epoch in range(num_epochs):
    indices = np.arange(num_samples)
    np.random.shuffle(indices)
    access_order.extend(indices)

# 只取前100个访问样本
access_order = access_order[:1300]

# 横轴为访问顺序索引
x = np.arange(len(access_order))

# 设置字体
plt.rcParams.update({'font.size': 30})
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 创建图形和子图布局
fig = plt.figure(figsize=(8, 6), constrained_layout=True)
gs = gridspec.GridSpec(1, 2, width_ratios=[4, 1], wspace=0.05, figure=fig)

# 主图：访问顺序散点图
ax_main = plt.subplot(gs[0])
ax_main.scatter(x, access_order, s=20, zorder=3)
ax_main.set_xlabel('Access Order')
ax_main.set_ylabel('Sample Index')
ax_main.grid(True)

# 右侧投影图：样本索引的直方图
ax_hist = plt.subplot(gs[1], sharey=ax_main)
ax_hist.hist(access_order, bins=1300, orientation='horizontal', color='gray', alpha=0.7)
ax_hist.tick_params(labelleft=False)  # 不显示左侧刻度标签
ax_hist.set_xlabel('Count')

# plt.tight_layout()
plt.savefig("random_access_with_projection.pdf", bbox_inches='tight')
plt.show()
