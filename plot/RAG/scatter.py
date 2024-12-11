import pandas as pd
import matplotlib.pyplot as plt
import os

# 定义文件路径
file_path = 'filtered_crag_3.txt'

# 定义保存结果的列表
diffs = []

# 设置绘图样式
plt.style.use("bmh")
plt.rcParams.update({'font.size': 26})
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

    block_ids = block_ids[:100]

    # 生成访问索引折线图
    plt.figure(figsize=(14, 8))
    plt.plot(range(len(block_ids)), block_ids, marker='o', linestyle='-')
    plt.xlabel('Access Ordinal')
    plt.ylabel('Block ID')
    plt.title('Block ID Access Pattern')
    plt.grid(True)

    # 保存图表
    output_file = 'block_access_pattern.pdf'
    plt.savefig(output_file)
    plt.show()
    print(f"Plot saved as {output_file}")