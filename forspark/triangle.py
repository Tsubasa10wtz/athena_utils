import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random
from matplotlib import ticker

# 文件参数
total_size = 11 * 1024 ** 3  # 11GB
chunk_size = 131072  # 128KB
num_chunks = total_size // chunk_size  # 总块数

# 模拟3个epoch的随机访问
all_accessed = []
for epoch in range(3):
    chunks = list(range(num_chunks))
    random.shuffle(chunks)
    all_accessed.extend(chunks)

# 转换为实际offset（字节单位）
# offsets = [chunk * chunk_size for chunk in all_accessed]

offsets = [chunk for chunk in all_accessed]


# 计算相邻offset的差值（绝对值）
deltas = np.abs(np.diff(offsets))

# 设置分桶参数
max_delta = np.max(deltas)
min_delta = np.min(deltas)
print(f"Delta range: [{min_delta:,}, {max_delta:,}] bytes")

# 使用对数分桶（因为差值可能跨度很大）
log_bins = np.linspace(min(deltas), max(deltas), 50)

# 创建图表
plt.figure(figsize=(18, 6))

# 绘制直方图
plt.hist(deltas, bins=log_bins, color='skyblue', edgecolor='black', alpha=0.7)

# 设置刻度格式
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(
    lambda x, _: f"{x:,.0f}"))  # 显示完整数字

# 标签和标题
plt.title('Distribution of Offset Differences', fontsize=32)
plt.xlabel('Absolute Difference (bytes)', fontsize=24)
plt.ylabel('Count', fontsize=24)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# 添加网格线
plt.grid(True, which="both", ls="--", alpha=0.3)

plt.tight_layout()
plt.show()

# 打印统计信息
print("\nDelta Statistics:")
print(f"Median delta: {np.median(deltas):,.0f} bytes")
print(f"Mean delta: {np.mean(deltas):,.0f} bytes")
print(f"Max delta: {max_delta:,} bytes")
print(f"Min delta: {min_delta:,} bytes")