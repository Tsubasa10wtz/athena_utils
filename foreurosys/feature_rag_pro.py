import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import gridspec

# 定义文件路径
file_path = '/Users/wangtianze/直博/项目/Athena/athena/plot/RAG/filtered_triviaqa_diskann_1221.txt'

# 设置绘图样式
plt.rcParams.update({'font.size': 30})
plt.rcParams['font.family'] = 'Arial Unicode MS'

# 读取文件并处理
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    block_ids = []

    # 提取 Offset 并计算 block ID
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
                    continue

    # 截取前 1300 个 block ID
    block_ids = block_ids[:1300]
    access_order = list(range(len(block_ids)))

    # 创建图形与子图布局
    fig = plt.figure(figsize=(8, 6), constrained_layout=True)
    gs = gridspec.GridSpec(1, 2, width_ratios=[4, 1], wspace=0.05, figure=fig)

    # 主图：访问顺序散点图
    ax_main = plt.subplot(gs[0])
    ax_main.scatter(access_order, block_ids, s=20, zorder=3)
    ax_main.set_xlabel('Access Order')
    ax_main.set_ylabel('Block ID')
    ax_main.grid(True)

    # 投影图：右侧直方图（细粒度桶）
    ax_hist = plt.subplot(gs[1], sharey=ax_main)
    bin_width = 1  # 每个桶包含 1 个 block_id，可根据需要调成 2、5、10 等
    min_block = min(block_ids)
    max_block = max(block_ids)
    bins = range(min_block, max_block + bin_width, bin_width)
    ax_hist.hist(block_ids, bins=bins, orientation='horizontal', color='gray', alpha=0.7)
    ax_hist.tick_params(labelleft=False)
    ax_hist.set_xlabel('Count')

    # plt.tight_layout()
    plt.savefig("rag_access_with_projection.pdf", bbox_inches='tight')
    plt.show()
