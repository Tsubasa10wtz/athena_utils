import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib import ticker
from collections import Counter

# 定义文件路径
file_path = 'filtered_triviaqa_diskann.txt'

# 设置绘图样式
plt.style.use("fivethirtyeight")
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 读取 filtered_triviaqa_diskann.txt 文件
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 提取每一行的块编号（Block ID）
    block_ids = []

    for line in lines:
        parts = line.split(',')
        for part in parts:
            if "Offset:" in part:
                offset_str = part.split(':')[1].strip()
                offset = int(offset_str)
                block_id = offset // (4 * 1024 * 1024)  # 计算块编号
                block_ids.append(block_id)

    # block_ids = block_ids[:100000]

    # 使用 Counter 统计每个 block_id 的出现次数
    counter = Counter(block_ids)

    # 将 block_id 按照出现次数从大到小排序
    sorted_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)



    # 提取排序后的 block_id 和对应的出现次数
    sorted_block_ids, sorted_counts = zip(*sorted_counts)

    # 计算 CDF（累积分布函数）
    total_count = sum(sorted_counts)
    cdf = np.cumsum(sorted_counts) / total_count

    # 计算前 50% 和后 50% 的出现总次数
    half_index = len(sorted_counts) // 2
    first_half_sum = sum(sorted_counts[:half_index])  # 前 50% 的总次数
    second_half_sum = sum(sorted_counts[half_index:])  # 后 50% 的总次数

    # 打印结果
    print(f"Total count of the first 50% Block IDs: {first_half_sum}")
    print(f"Total count of the second 50% Block IDs: {second_half_sum}")

    # 绘制 CDF 图
    plt.figure(figsize=(14, 6))
    plt.plot(np.arange(len(cdf)) / len(cdf), cdf, linestyle='-', color='b')

    # 设置图表标题和标签
    # plt.title('CDF of Block IDs')
    plt.xlabel('Ratio of Item', fontsize=30)
    plt.ylabel('CDF', fontsize=30)

    # 设置 x 轴和 y 轴的刻度字体大小
    plt.tick_params(axis='x', labelsize=20)  # x 轴刻度字体大小
    plt.tick_params(axis='y', labelsize=20)  # y 轴刻度字体大小

    # 显示网格
    plt.grid(True)

    # 调整坐标轴刻度
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(0.1))

    plt.tight_layout()

    # 保存图表为 PDF
    plt.savefig('skewed_cdf.pdf', facecolor='white', bbox_inches='tight')

    # 显示图表
    plt.show()