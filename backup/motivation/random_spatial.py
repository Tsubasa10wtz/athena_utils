import numpy as np
import matplotlib.pyplot as plt

# 生成 10 段随机打乱的 0-1299 序列
segments = [np.random.permutation(1300) for _ in range(100)]
ids = np.concatenate(segments)

# 计算频次
# frequency = np.bincount(ids)

# 累积分布计算
sorted_ids = np.sort(ids)
cdf = np.arange(1, len(sorted_ids) + 1) / len(sorted_ids)

# 绘制图表
plt.style.use("fivethirtyeight")
plt.rcParams['font.family'] = 'Arial Unicode MS'

fig, ax1 = plt.subplots(figsize=(14, 6))

# 绘制直方图（左轴）
ax1.hist(ids, bins=1299, alpha=0.6, label='Count', color='#003a75')  # 默认颜色
ax1.set_xlabel('IDs', fontsize=44, color='black')  # 黑色字体
# ax1.set_ylabel('Count', color='black', fontsize=36)  # 黑色字体
ax1.tick_params(axis='y', labelcolor='black')
ax1.tick_params(axis='x', labelsize=24, colors='black')  # 黑色刻度
ax1.set_ylim(0, 100 * 1.1)  # 动态设置直方图的最大范围

# 创建右轴（第二个 y 轴）
ax2 = ax1.twinx()

# 绘制 CDF（右轴）
cdf_plot, = ax2.plot(sorted_ids, cdf, label='CDF', linestyle='-', alpha=0.8, color='#9f0000')  # 使用红色标识
# ax2.set_ylabel('CDF', color='black', fontsize=36)  # 黑色字体
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_ylim(0, 1.1)  # CDF 固定范围

# 合并图例
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + [cdf_plot]  # 添加 CDF 的线条句柄
labels = labels1 + ['CDF']      # 添加 CDF 的标签

plt.legend(handles, labels, loc='upper right', fontsize=28)

# 修改 X 轴刻度字体
ax1.tick_params(axis='x', labelsize=30)  # 设置 X 轴刻度字体大小为 16
# 修改左 Y 轴刻度字体
ax1.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小为 16
# 修改右 Y 轴刻度字体
ax2.tick_params(axis='y', labelsize=30)  # 设置右 Y 轴刻度字体大小为 16

# 添加网格和样式
ax1.grid(alpha=0.4)

plt.tight_layout()
# plt.show()

plt.savefig('random_spatial.pdf', facecolor='white', bbox_inches='tight')
