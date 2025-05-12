import os

import numpy as np

from sensitivity.ks.ks_test import calculate_diff_mean_and_variance, triangular_cdf
from scipy.stats import kstest, ks_2samp

# 定义文件路径
file_path = '/Users/wangtianze/直博/项目/Athena/athena/plot/RAG/filtered_triviaqa_diskann_1221.txt'

# 定义存储块号差值的列表
diffs = []

# 假设 c 已知（三角分布的参数）
c = 368  # 这个值可以根据你的数据进行调整

# 检查文件是否存在
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    # 读取文件并提取块号
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 提取每一行的块号（Block ID）
    block_ids = []

    for line in lines:
        parts = line.split(',')
        for part in parts:
            if "Offset:" in part:
                offset_str = part.split(':')[1].strip()
                offset = int(offset_str)
                block_id = offset // (4 * 1024 * 1024)  # 计算块编号（每块 4MB）
                block_ids.append(block_id)

block_ids = block_ids[:100]
unique_elements, counts = np.unique(block_ids, return_counts=True)

print(counts)
# 在这里，构造一个和 counts 长度一致、值全是 counts 的最大值的数组
max_count = np.max(counts)
uniform_array = np.full_like(counts, max_count)  # 或者 np.repeat(max_count, len(counts))

# 使用ks_2samp比较 counts 和 uniform_array
result = ks_2samp(counts, uniform_array)
print(result.pvalue)