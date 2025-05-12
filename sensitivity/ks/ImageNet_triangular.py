import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt, ticker
from scipy.stats import kstest

from sensitivity.ks.ks_test import calculate_diff_mean_and_variance, triangular_cdf

# 设置参数
c = 1300
base_sequence = np.arange(0, 1300)  # 0-1299 的序列
print(len(base_sequence))
np.random.seed(45)  # 设置随机种子，保证结果一致

# 生成打乱后的序列并重复拼接
shuffled_sequences = [np.random.permutation(base_sequence) for _ in range(10)]
ids = np.concatenate(shuffled_sequences)

# 统计 p 值分布
p_values = []
batch_size = 100

# 按批次处理数据
for i in range(0, len(ids), batch_size):
    # 提取一个批次的数据
    batch = ids[i:i + batch_size]
    if len(batch) < batch_size:
        break  # 忽略不足一个批次的数据

    # 计算当前批次的差值
    diff = calculate_diff_mean_and_variance(batch)

    # 执行 K-S 检验
    result = kstest(diff, triangular_cdf, args=(c,))
    p_values.append(result.pvalue)

# 统计 p 值 >= 0.01 的数量
count_ge_0_01 = sum(1 for p in p_values if p >= 0.01)

# 统计 p 值 < 0.01 的数量
count_lt_0_01 = sum(1 for p in p_values if p < 0.01)

# 统计 p 值 >= 0.05 的数量
count_ge_0_05 = sum(1 for p in p_values if p >= 0.05)

# 统计 p 值 < 0.05 的数量
count_lt_0_05 = sum(1 for p in p_values if p < 0.05)



# 输出结果
print(f"Number of p-values >= 0.01: {count_ge_0_01}")
print(f"Number of p-values < 0.01: {count_lt_0_01}")
print(f"Number of p-values >= 0.05: {count_ge_0_05}")
print(f"Number of p-values < 0.05: {count_lt_0_05}")
print(f"P-values: {p_values}")