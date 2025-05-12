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
plt.rcParams['font.family'] = 'Arial Unicode MS'  # 确保支持中文字体

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
                    block_id = offset // (4 * 1024 * 1024)  # 计算块编号
                    block_ids.append(block_id)
                except ValueError:
                    print(f"无法转换Offset为整数: {offset_str}")

    if not block_ids:
        print("没有提取到任何block_id。")
    else:
        # 统计每个block_id出现的次数
        block_id_counts = pd.Series(block_ids).value_counts()

        # 统计出现次数的分布，即每个count有多少个id
        frequency_counts = block_id_counts.value_counts().sort_index()

        # 在 0 处添加一个值为 0 的条目
        frequency_counts.loc[0] = 0
        frequency_counts = frequency_counts.sort_index()  # 确保索引顺序正确

        # 计算CDF
        cdf = frequency_counts.cumsum() / frequency_counts.sum()

        cdf = pd.concat([pd.Series({0: 0}), cdf])

        cdf.loc[cdf.index.max() + 200] = 1  # 在最后添加延伸点，值为 1

        # 打印一些统计信息（可选）
        print(cdf)

        # 绘制CDF
        plt.figure(figsize=(14, 6))
        plt.plot(cdf.index, cdf.values, linestyle='-', linewidth=10)
        plt.xlabel('Count', fontsize=44)
        plt.ylabel('CDF', fontsize=44)
        plt.grid(True)

        plt.tick_params(axis='x', labelsize=30)  # x 轴刻度字体大小
        plt.tick_params(axis='y', labelsize=30)  # y 轴刻度字体大小

        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.2))  # 每隔 60 一格
        plt.gca().set_ylim(0, 1 * 1.1)  # 直方图的最大范围同步





        # 设置x轴主刻度为整数
        plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

        plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1000))  # 每隔 60 一格
        plt.gca().set_xlim(0, 7000 * 1.1)  # 直方图的最大范围同步

        plt.tight_layout()
        plt.savefig('RAG_temporal.pdf', facecolor='white', bbox_inches='tight')
        plt.show()