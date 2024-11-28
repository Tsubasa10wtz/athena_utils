import numpy as np
from scipy.stats import kstest
import os

# 定义文件路径
file_path = 'filtered_log.txt'

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

    # 如果读取到的块编号数小于2，则没有足够的数据进行差值计算
    if len(block_ids) < 2:
        print("Not enough data to calculate differences.")
    else:
        # 计算相邻块编号之间的差值
        for i in range(1, len(block_ids)):
            diff = abs(block_ids[i] - block_ids[i - 1])
            diffs.append(diff)

        # 输出前50个差值作为检查
        diff_list = diffs[:1000]
        print("First 50 differences:", diff_list)

        # 执行KS检验，使用三角分布的累积分布函数（CDF）
        def triangular_cdf(x, c):
            return np.where(x < 0, 0, np.where(x > c, 1, ((2*x*c - x**2) / c**2)))

        # 执行KS检验
        result = kstest(diff_list, triangular_cdf, args=(c,))
        print('KS statistic:', result.statistic)
        print('p-value:', result.pvalue)
