import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker

# 使用顺序序列
ids = np.arange(0, 1300)
# ids = np.random.permutation(1300)

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

# 累积分布计算
sorted_diffs = np.sort(diff_list)
cdf = np.arange(1, len(sorted_diffs) + 1) / len(sorted_diffs)


print(diff_list)

print(cdf)


# 定义格式化函数
def thousands(x, pos):
    return f'{x * 1e-3:,.0f}'

# 绘制图表
plt.style.use("fivethirtyeight")
plt.rcParams['font.family'] = 'Arial Unicode MS'

fig, ax1 = plt.subplots(figsize=(14, 6))

# 绘制直方图（左轴）
ax1.hist(diff_list, bins=1, alpha=0.6, label='Count', color='#003a75')  # 默认颜色
ax1.set_xlabel('Gap', fontsize=36, color='black')  # 黑色字体
ax1.set_ylabel('Count', color='black', fontsize=36)  # 黑色字体
ax1.tick_params(axis='y', labelcolor='black')
ax1.tick_params(axis='x', labelsize=24, colors='black')  # 黑色刻度
ax1.yaxis.set_major_locator(ticker.MultipleLocator(350))  # 每隔 45 一格
ax1.set_ylim(0, 1400 * 1.1)  # 直方图的最大范围同步

ax1.set_xlim(-50, 1300)  # 直方图的最大范围同步

# 创建右轴（第二个 y 轴）
ax2 = ax1.twinx()

for i in range(2, 1300):
    sorted_diffs = np.append(sorted_diffs, i)
    cdf = np.append(cdf, 1.0)


# 绘制 CDF（右轴）
cdf_plot, = ax2.plot(sorted_diffs, cdf, label='CDF', linestyle='-', alpha=0.8, color='#9f0000')  # 使用蓝色标识
# ax2.set_ylabel('CDF', color='black', fontsize=36)  # 黑色字体
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_ylim(0, 1.1)  # CDF 固定范围



# 合并图例
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + [cdf_plot]  # 添加 CDF 的线条句柄
labels = labels1 + ['CDF']      # 添加 CDF 的标签

# plt.legend(handles, labels, loc='upper right', fontsize=20)
plt.legend(handles, labels, loc='upper right', fontsize=28)
# plt.legend(handles1, labels1, loc='upper right', fontsize=20)

# 修改 X 轴刻度字体
ax1.tick_params(axis='x', labelsize=30)  # 设置 X 轴刻度字体大小为 16
# 修改左 Y 轴刻度字体
ax1.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小为 16
# 修改右 Y 轴刻度字体
ax2.tick_params(axis='y', labelsize=30)  # 设置右 Y 轴刻度字体大小为 16
# 在 CDF 到达最大值时添加水平直线


# 添加网格和样式
ax1.grid(alpha=0.4)

plt.tight_layout()
# plt.show()
plt.savefig('sequential_temporal.pdf', facecolor='white', bbox_inches='tight')