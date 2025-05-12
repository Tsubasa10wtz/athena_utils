import pandas as pd
import matplotlib.pyplot as plt
import os

# 定义文件路径
file_path = '/Users/wangtianze/直博/项目/Athena/athena/plot/RAG/filtered_triviaqa_diskann_1221.txt'

# 设置绘图样式
plt.rcParams.update({'font.size': 30})
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 读取 filtered_crag_3.txt 文件
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    block_ids = []

    # 提取每一行中的 Offset 并计算 block ID
    for line in lines:
        parts = line.split(',')
        for part in parts:
            if "Offset:" in part:
                try:
                    offset_str = part.split(':')[1].strip()
                    offset = int(offset_str)
                    block_id = offset // (4 * 1024 * 1024)
                    block_ids.append(block_id)
                except (IndexError, ValueError):
                    continue  # 安全处理可能的格式问题


    block_ids = block_ids[0:1300]
    # 构造横轴（访问顺序）
    access_order = list(range(len(block_ids)))

    # 绘图：访问顺序图
    plt.figure(figsize=(8, 6))
    plt.scatter(access_order, block_ids, s=20, zorder=3)
    plt.xlabel('Access Order')
    plt.ylabel('Block ID')
    plt.grid(True)
    plt.tight_layout()
    # plt.savefig("rag_access.pdf", bbox_inches='tight')
    plt.show()
