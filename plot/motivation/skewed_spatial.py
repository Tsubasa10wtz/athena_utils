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
# plt.style.use("fivethirtyeight")
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

    # 如果读取到的块编号数小于2，则没有足够的数据进行差值计算
    if len(block_ids) < 2:
        print("Not enough data to calculate differences.")
    else:
        # 计算相邻块编号之间的差值
        for i in range(1, len(block_ids)):
            diff = abs(block_ids[i] - block_ids[i - 1])
            diffs.append(diff)

        # 找出最大差值
        max_diff = max(diffs)
        print(f"Maximum difference: {max_diff}")

        # 计算差值的均值和方差
        mean_diff = pd.Series(diffs).mean()
        variance_diff = pd.Series(diffs).var()
        print(f"Mean of differences: {mean_diff}")
        print(f"Variance of differences: {variance_diff}")

        # 绘制图表
        fig, ax1 = plt.subplots(figsize=(10, 6))

        bins = np.arange(0, 367, 3)


        # 绘制直方图（左轴）
        ax1.hist(diffs, bins=bins, alpha=0.6, label='Count', color='#003a75')
        ax1.set_xlabel('Gap', fontsize=44, color='black')
        ax1.set_ylabel('Count', color='black', fontsize=44)
        ax1.tick_params(axis='y', labelcolor='black')
        ax1.tick_params(axis='x', labelsize=24, colors='black')
        # ax1.yaxis.set_major_locator(ticker.MultipleLocator(1250))  # 每隔 1250 一格
        ax1.set_ylim(0, 130000 * 1.1)  # 动态设置Y轴范围

        # 删除右轴和CDF线条部分
        # 删除创建右侧 Y 轴
        # ax2 = ax1.twinx()

        # 删除 CDF 绘制
        # cdf_plot, = ax2.plot(sorted_diffs, cdf, label='CDF', linestyle='-', alpha=0.8, color='#9f0000')
        # ax2.set_ylabel('CDF', color='black', fontsize=36)
        # ax2.set_ylim(0, 1.1)  # CDF 固定范围

        # 合并图例
        handles1, labels1 = ax1.get_legend_handles_labels()
        # handles2, labels2 = ax2.get_legend_handles_labels()
        # handles = handles1 + [cdf_plot]  # 添加 CDF 的线条句柄
        # labels = labels1 + ['CDF']      # 添加 CDF 的标签
        plt.legend(handles1, labels1, loc='upper right', fontsize=28)

        # 修改 X 轴刻度字体
        ax1.tick_params(axis='x', labelsize=30)  # 设置 X 轴刻度字体大小为 16
        # 修改左 Y 轴刻度字体
        ax1.tick_params(axis='y', labelsize=30)  # 设置左 Y 轴刻度字体大小为 16

        # 添加网格和样式
        ax1.grid(alpha=0.4)

        # 调整布局
        plt.tight_layout()

        # 显示图表
        # plt.show()
        plt.savefig('RAG_spatial.pdf', facecolor='white', bbox_inches='tight')