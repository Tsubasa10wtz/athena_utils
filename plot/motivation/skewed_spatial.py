import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib import ticker

# 定义文件路径
file_path = 'filtered_triviaqa_diskann.txt'

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

    # 设置图表
    fig, ax1 = plt.subplots(figsize=(14, 6))



    # 绘制直方图（左轴）
    ax1.hist(block_ids, bins=368, alpha=0.6, label='Count', color='#003a75')
    ax1.set_xlabel('IDs', fontsize=44, color='black')
    ax1.set_ylabel('Count', color='black', fontsize=44, labelpad=40)  # 黑色字体
    ax1.tick_params(axis='y', labelcolor='black')
    ax1.tick_params(axis='x', labelsize=24, colors='black')
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(2000))
    ax1.set_ylim(0, 7000 * 1.1)  # 动态设置Y轴范围

    # 图例
    handles1, labels1 = ax1.get_legend_handles_labels()
    plt.legend(handles1, labels1, loc='upper right', fontsize=28)

    # 修改 X 轴刻度字体
    ax1.tick_params(axis='x', labelsize=30)  # 设置 X 轴刻度字体大小
    # 修改左 Y 轴刻度字体
    ax1.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小

    # 添加网格和样式
    ax1.grid(alpha=0.4)

    # 调整布局
    plt.tight_layout()

    # 保存图表
    plt.savefig('skewed_spatial.pdf', facecolor='white', bbox_inches='tight')