import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# 定义文件路径
file_path = 'filtered_log2.txt'

# 定义保存结果的列表
diffs = []

# 设置绘图样式
plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 40})
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 读取 filtered_log.txt 文件
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

        # 计算差值的均值和方差
        mean_diff = pd.Series(diffs).mean()
        variance_diff = pd.Series(diffs).var()
        print(f"Mean of differences: {mean_diff}")
        print(f"Variance of differences: {variance_diff}")

        # 计算 CDF 数据
        sorted_diffs = np.sort(diffs)  # 按升序排序
        cdf = np.arange(1, len(sorted_diffs) + 1) / len(sorted_diffs)  # 累积分布百分比

        # 绘制 CDF 图
        plt.figure(figsize=(12, 6))
        plt.rcParams.update({'font.size': 33})

        # 使用点绘制 CDF
        plt.plot(sorted_diffs, cdf, marker='.', linestyle='none')

        # 设置坐标轴标签
        plt.xlabel('Gap')
        plt.ylabel('CDF')

        plt.grid(True)
        plt.tight_layout()

        # 保存为 PDF 文件
        plt.savefig('block_diff_cdf_point.pdf', facecolor='white', bbox_inches='tight')

        # 显示图表
        plt.show()