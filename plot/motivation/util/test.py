from collections import defaultdict

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib import ticker

# 定义文件路径
file_path = '../filtered_triviaqa_diskann_1221.txt'

def longest_unique_subsequence(seq):
    seen = {}
    max_len = 0
    start = 0
    max_start = 0
    max_end = 0

    for i, item in enumerate(seq):
        if item in seen and seen[item] >= start:
            start = seen[item] + 1
        seen[item] = i
        if i - start + 1 > max_len:
            max_len = i - start + 1
            max_start = start
            max_end = i

    return max_len, max_start, max_end

def longest_simple_balanced_subsequence(seq):
    count = defaultdict(int)
    max_len = 0
    left = 0
    max_start = 0
    max_end = 0

    for right, item in enumerate(seq):
        count[item] += 1

        while True:
            current_counts = list(count.values())
            if not current_counts:
                break
            max_count = max(current_counts)
            min_count = min(current_counts)
            if max_count - min_count <= 1:
                break
            # 否则收缩左边界
            left_item = seq[left]
            count[left_item] -= 1
            if count[left_item] == 0:
                del count[left_item]
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_start = left
            max_end = right

    return max_len, max_start, max_end



# 读取 filtered_triviaqa_diskann.txt 文件
if not os.path.exists(file_path):
    print(f"文件未找到: {file_path}")
else:
    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 提取每一行的块编号（Block ID），并计算差值
    block_ids = []

    for line in lines:
        parts = line.split(',')
        for part in parts:
            if "Offset:" in part:
                offset_str = part.split(':')[1].strip()
                try:
                    offset = int(offset_str)
                    block_id = offset // 4096  # 计算块编号
                    block_ids.append(block_id)
                except ValueError:
                    print(f"无法转换Offset为整数: {offset_str}")

    max_len, start_idx, end_idx = longest_simple_balanced_subsequence(block_ids)
    print(f"不含重复项的连续子序列的最大长度是: {max_len}")
    print(f"起始地址（索引）: {start_idx}")
    print(f"结束地址（索引）: {end_idx}")
    print(f"最长子序列: {block_ids[start_idx:end_idx + 1]}")

    # max_seq = block_ids[start_idx:end_idx + 1]
    print(max(block_ids))
    max_seq =  block_ids[start_idx:start_idx+311]
    print(f"最长子序列: {max_seq}")

    # ======= 差值分析和可视化 =======
    # if len(max_seq) < 2:
    #     print("Not enough data to calculate differences.")
    # else:
    #     diffs = []
    #     for i in range(1, len(max_seq)):
    #         diff = abs(max_seq[i] - max_seq[i - 1])
    #         diffs.append(diff)
    #
    #     max_diff = max(diffs)
    #     mean_diff = pd.Series(diffs).mean()
    #     variance_diff = pd.Series(diffs).var()
    #
    #     print(f"Maximum difference: {max_diff}")
    #     print(f"Mean of differences: {mean_diff}")
    #     print(f"Variance of differences: {variance_diff}")
    #
    #     # 绘图
    #     fig, ax1 = plt.subplots(figsize=(10, 6))
    #     bins = np.arange(0, 5000, 3)
    #
    #     ax1.hist(diffs, bins=bins, alpha=0.6, label='Count', color='#003a75')
    #     ax1.set_xlabel('Gap', fontsize=44, color='black')
    #     ax1.set_ylabel('Count', color='black', fontsize=44)
    #     ax1.tick_params(axis='y', labelcolor='black')
    #     ax1.tick_params(axis='x', labelsize=24, colors='black')
    #     ax1.set_ylim(0, int(1.2 * max(np.histogram(diffs, bins=bins)[0])))
    #
    #     # 图例
    #     handles1, labels1 = ax1.get_legend_handles_labels()
    #     plt.legend(handles1, labels1, loc='upper right', fontsize=28)
    #
    #     # 刻度和网格
    #     ax1.tick_params(axis='x', labelsize=30)
    #     ax1.tick_params(axis='y', labelsize=30)
    #     ax1.grid(alpha=0.4)
    #
    #     # 布局和保存
    #     plt.tight_layout()
    #     plt.show()