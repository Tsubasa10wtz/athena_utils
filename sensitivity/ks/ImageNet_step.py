import numpy as np
from scipy.stats import kstest, ks_2samp

from sensitivity.ks.ks_test import step_cdf

# 设置参数
base_sequence = np.arange(0, 1300)  # 基础序列 0-1299
batch_size = 150  # 每个批次大小
np.random.seed(45)  # 设置随机种子，保证结果一致

# 生成打乱后的序列并重复拼接
shuffled_sequences = [np.random.permutation(base_sequence) for _ in range(1)]
ids = np.concatenate(shuffled_sequences)

p_values = []

# 按批次处理数据
for i in range(0, len(ids), batch_size):
    # 提取一个批次的数据
    batch = ids[i:i + batch_size]
    if len(batch) < batch_size:
        break  # 忽略不足一个批次的数据

    # 统计每个元素在当前批次中的出现次数
    unique_elements, counts = np.unique(batch, return_counts=True)

    # 在这里，构造一个和 counts 长度一致、值全是 counts 的最大值的数组
    max_count = np.max(counts)
    uniform_array = np.full_like(counts, max_count)  # 或者 np.repeat(max_count, len(counts))

    # 使用ks_2samp比较 counts 和 uniform_array
    result = ks_2samp(counts, uniform_array)
    p_values.append(result.pvalue)


# 统计 p 值 >= 0.05 的数量
count_ge_0_05 = sum(1 for p in p_values if p >= 0.05)

# 统计 p 值 < 0.05 的数量
count_lt_0_05 = sum(1 for p in p_values if p < 0.05)

# 输出结果
print(f"Number of p-values >= 0.05: {count_ge_0_05}")
print(f"Number of p-values < 0.05: {count_lt_0_05}")
print(f"P-values: {p_values}")







