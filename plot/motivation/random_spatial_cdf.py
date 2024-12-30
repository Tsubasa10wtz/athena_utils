import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import ticker

# plt.style.use("fivethirtyeight")
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 生成 10 段随机打乱的 0-1299 序列
segments = [np.random.permutation(1300) for _ in range(100)]
ids = np.concatenate(segments)

# 使用 Counter 统计每个 ID 的出现次数
counter = Counter(ids)

# 将 ID 按照出现次数从大到小排序
sorted_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)

# 提取排序后的 IDs 和对应的出现次数
sorted_ids, sorted_counts = zip(*sorted_counts)

# 计算 CDF（累积分布函数）
total_count = sum(sorted_counts)
cdf = np.cumsum(sorted_counts) / total_count

# 计算前 50% 和后 50% 的出现总次数
half_index = len(sorted_counts) // 2
first_half_sum = sum(sorted_counts[:half_index])  # 前 50% 的总次数
second_half_sum = sum(sorted_counts[half_index:])  # 后 50% 的总次数

# 打印结果
print(f"Total count of the first 50% IDs: {first_half_sum}")
print(f"Total count of the second 50% IDs: {second_half_sum}")

# 绘制 CDF 图
plt.figure(figsize=(14, 6))

plt.plot(np.arange(len(cdf)) / len(cdf), cdf, marker='.', linestyle='-', color='b')

# 设置图表标题和标签
# plt.title('CDF of IDs')
plt.xlabel('Ratio of Item', fontsize=44)
plt.ylabel('CDF', fontsize=44)

# 设置 x 轴和 y 轴的刻度字体大小
plt.tick_params(axis='x', labelsize=24)  # x 轴刻度字体大小
plt.tick_params(axis='y', labelsize=24)  # y 轴刻度字体大小

# 显示网格
plt.grid(True)

# 调整坐标轴刻度
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(0.1))

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.2))

plt.tight_layout()

# 保存图表为 PDF
plt.savefig('random_cdf.pdf', facecolor='white', bbox_inches='tight')

# 显示图表
plt.show()