import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.ticker import MultipleLocator

# 生成 100 段随机打乱的 0-1299 序列
segments = [np.random.permutation(1300) for _ in range(100)]
ids = np.concatenate(segments)

first_N = 1300 * 99 + 750
ids = ids[:first_N]

# 确保 ids 的长度为 1300 * 100 = 130000
print(f"ids 的总长度: {len(ids)}")

plt.style.use("fivethirtyeight")
plt.rcParams['font.family'] = 'Arial Unicode MS'  # 确保支持中文字体

# 统计每个 id 出现的次数
id_counts = pd.Series(ids).value_counts().sort_index()

# 打印一些统计信息
print("每个 id 出现的次数前10项:")
print(id_counts.head(10))

# 统计出现次数的分布，即每个 count 有多少个 id
frequency_counts = id_counts.value_counts().sort_index()

# 打印出现次数的分布
print("\n出现次数的分布:")
print(frequency_counts)

# 构造完整的 Count 区间
min_count = frequency_counts.index.min()
max_count = frequency_counts.index.max()

# 如果需要从 0 开始，包括 0
full_range = range(0, max_count + 1)

# 重新索引 frequency_counts，填补缺失的 Count 值为 0
frequency_counts = frequency_counts.reindex(full_range, fill_value=0)

# 打印重新索引后的出现次数分布（可选）
print("\n重新索引后的出现次数分布:")
print(frequency_counts)

# 计算 CDF
cdf = frequency_counts.cumsum() / frequency_counts.sum()

# 打印 CDF
print("\nCDF:")
print(cdf)

for i in range(101, 111):
    cdf[i] = 1.000000



# 绘制 CDF
plt.figure(figsize=(14, 6))
plt.plot(cdf.index, cdf.values, linestyle='-')
plt.xlabel('Count', fontsize=30)
plt.ylabel('CDF', fontsize=30)
plt.grid(True)

plt.tick_params(axis='x', labelsize=20)  # x 轴刻度字体大小
plt.tick_params(axis='y', labelsize=20)  # y 轴刻度字体大小


ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(20))
plt.xlim(0, 110)

plt.tight_layout()
plt.show()