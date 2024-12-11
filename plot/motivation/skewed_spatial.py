import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib import ticker

# 定义文件路径
file_path = 'filtered_crag_3.txt'

# 定义保存结果的列表
diffs = []

# 设置绘图样式
plt.style.use("fivethirtyeight")
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 读取 filtered_crag_3.txt 文件
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
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
                offset = int(offset_str)
                block_id = offset // (4 * 1024 * 1024)  # 计算块编号
                block_ids.append(block_id)

    sorted_ids = np.sort(block_ids)
    cdf = np.arange(1, len(sorted_ids) + 1) / len(sorted_ids)

    # 绘制图表
    fig, ax1 = plt.subplots(figsize=(10, 8))

    # 绘制直方图（左轴）
    ax1.hist(block_ids, bins=368, alpha=0.6, label='Frequency Distribution', color='#003a75')
    ax1.set_xlabel('Gap', fontsize=24, color='black')
    ax1.set_ylabel('Count', color='black', fontsize=24)
    ax1.tick_params(axis='y', labelcolor='black')
    ax1.tick_params(axis='x', labelsize=12, colors='black')
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(160))
    ax1.set_ylim(0, 800 * 1.1)  # 动态设置Y轴范围

    # 创建右轴（第二个 y 轴）
    ax2 = ax1.twinx()

    # 绘制 CDF（右轴）
    cdf_plot, = ax2.plot(sorted_ids, cdf, label='CDF', linestyle='-', alpha=0.8, color='#9f0000')
    ax2.set_ylabel('CDF', color='black', fontsize=24)
    ax2.tick_params(axis='y', labelcolor='black')
    ax2.set_ylim(0, 1.1)  # CDF 固定范围

    # 合并图例
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    handles = handles1 + [cdf_plot]
    labels = labels1 + ['CDF']

    plt.legend(handles, labels, loc='upper right', fontsize=20)

    # 修改 X 轴刻度字体
    ax1.tick_params(axis='x', labelsize=16)  # 设置 X 轴刻度字体大小为 16
    # 修改左 Y 轴刻度字体
    ax1.tick_params(axis='y', labelsize=16)  # 设置左 Y 轴刻度字体大小为 16
    # 修改右 Y 轴刻度字体
    ax2.tick_params(axis='y', labelsize=16)  # 设置右 Y 轴刻度字体大小为 16

    # 添加网格和样式
    ax1.grid(alpha=0.4)

    # 调整布局
    plt.tight_layout()

    # 显示图表
    plt.show()

