import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

ids = np.arange(0, 1300)

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
ax1.set_ylim(0, 1 * 1.1)  # 动态设置直方图的最大范围
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))  # y 轴每隔 1 显示一个刻度

# 图例
handles1, labels1 = ax1.get_legend_handles_labels()
plt.legend(handles1, labels1, loc='upper right', fontsize=28)

# 修改 X 轴刻度字体
ax1.tick_params(axis='x', labelsize=30)  # 设置 X 轴刻度字体大小为 16
# 修改左 Y 轴刻度字体
ax1.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小为 16

# 添加网格和样式
ax1.grid(alpha=0.4)

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig('sequential_spatial.pdf', facecolor='white', bbox_inches='tight')