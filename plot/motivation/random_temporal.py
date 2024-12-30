import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker

# 生成 10 段随机打乱的 0-1299 序列
segments = [np.random.permutation(1300) for _ in range(100)]
ids = np.concatenate(segments)

# 计算频次
frequency = np.bincount(ids)
sorted_frequency = np.sort(frequency)[::-1]

# 计算累积分布的差值
def calculate_diff_mean_and_variance(numbers):
    diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]
    mean_diff = np.mean(diff_list)
    var_diff = np.var(diff_list)
    return diff_list, mean_diff, var_diff

diff_list, mean_diff, var_diff = calculate_diff_mean_and_variance(ids)

# 定义格式化函数
def thousands(x, pos):
    return f'{x * 1e-3:,.0f}'

# 绘制图表
# plt.style.use("fivethirtyeight")
plt.rcParams['font.family'] = 'Arial Unicode MS'

fig, ax1 = plt.subplots(figsize=(14, 6))

bins = np.arange(0, 1299, 10)

# 绘制直方图（左轴）
ax1.hist(diff_list, bins=bins, alpha=0.6, label='Count', color='#003a75')  # 默认颜色
ax1.set_xlabel('Gap', fontsize=44, color='black')  # 黑色字体
ax1.set_ylabel('Count', color='black', fontsize=44)  # 黑色字体
ax1.tick_params(axis='y', labelcolor='black')
ax1.tick_params(axis='x', labelsize=24, colors='black')  # 黑色刻度
ax1.yaxis.set_major_locator(ticker.MultipleLocator(500))  # 每隔 60 一格
ax1.set_ylim(0, 2200 * 1.1)  # 直方图的最大范围同步
ax1.set_xlim(-50, 1300)  # 直方图的最大范围同步

# 删除右轴和CDF线条部分
# 1. 删除右侧 Y 轴的创建
# 2. 删除 CDF 绘制代码

# 合并图例
handles1, labels1 = ax1.get_legend_handles_labels()

# 绘制图例
plt.legend(handles1, labels1, loc='upper right', fontsize=28)

# 修改 X 轴刻度字体
ax1.tick_params(axis='x', labelsize=30)  # 设置 X 轴刻度字体大小为 16
# 修改左 Y 轴刻度字体
ax1.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小为 16

# 添加网格和样式
ax1.grid(alpha=0.4)

plt.tight_layout()

# 保存图表
plt.savefig('random_temporal.pdf', facecolor='white', bbox_inches='tight')