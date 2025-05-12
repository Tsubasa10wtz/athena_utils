import os

import numpy as np

from sensitivity.ks.ks_test import calculate_diff_mean_and_variance, triangular_cdf
from scipy.stats import kstest

# 定义文件路径
file_path = '/Users/wangtianze/直博/项目/Athena/athena/plot/RAG/filtered_triviaqa_diskann_1221.txt'

# 定义存储块号差值的列表
diffs = []

# 提取每一行的块号（Block ID）
block_ids = []

# 假设 c 已知（三角分布的参数）
c = 368  # 这个值可以根据你的数据进行调整

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    # 读取文件并提取块号
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    for line in lines:
        parts = line.split(',')
        for part in parts:
            if "Offset:" in part:
                offset_str = part.split(':')[1].strip()
                offset = int(offset_str)
                block_id = offset // (4 * 1024 * 1024)  # 计算块编号（每块 4MB）
                block_ids.append(block_id)

ids = block_ids

ids = ids[:10000]

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