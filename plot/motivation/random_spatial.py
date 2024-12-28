import numpy as np
import matplotlib.pyplot as plt

# 生成 10 段随机打乱的 0-1299 序列
segments = [np.random.permutation(1300) for _ in range(100)]
ids = np.concatenate(segments)

# 绘制图表
plt.style.use("fivethirtyeight")
plt.rcParams['font.family'] = 'Arial Unicode MS'

fig, ax1 = plt.subplots(figsize=(14, 6))

# 绘制直方图（左轴）
ax1.hist(ids, bins=1299, alpha=0.6, label='Count', color='#003a75')  # 默认颜色
ax1.set_xlabel('IDs', fontsize=44, color='black')  # 黑色字体
ax1.set_ylabel('Count', color='black', fontsize=44, labelpad=40)  # 黑色字体
ax1.tick_params(axis='y', labelcolor='black')
ax1.tick_params(axis='x', labelsize=24, colors='black')  # 黑色刻度
ax1.set_ylim(0, 100 * 1.1)  # 动态设置直方图的最大范围

# 图例
handles1, labels1 = ax1.get_legend_handles_labels()
plt.legend(handles1, labels1, loc='upper right', fontsize=28)

# 修改 X 轴刻度字体
ax1.tick_params(axis='x', labelsize=30)  # 设置 X 轴刻度字体大小
# 修改左 Y 轴刻度字体
ax1.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小

# 添加网格和样式
ax1.grid(alpha=0.4)

plt.tight_layout()
# plt.show()

plt.savefig('random_spatial.pdf', facecolor='white', bbox_inches='tight')