import matplotlib.pyplot as plt
from collections import Counter

# 读取 filtered_log.txt 文件
with open('filtered_log.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# 用于存储每个块编号的计数
block_counts = Counter()

# 处理每一行，提取 Offset，计算块编号
for line in lines:
    # 找到 "Offset:" 后的数值
    parts = line.split(',')
    for part in parts:
        if "Offset:" in part:
            offset_str = part.split(':')[1].strip()
            offset = int(offset_str)

            # 计算块编号
            block_id = offset // (4 * 1024 * 1024)  # 除以 4MB
            block_counts[block_id] += 1
            break  # 每行只处理一个 Offset

# 获取块编号和其出现次数
block_ids = list(block_counts.keys())
counts = list(block_counts.values())

# 输出出现最多和最少的块编号和次数
most_common_block = block_counts.most_common(1)[0]  # 获取出现最多的块编号
least_common_block = min(block_counts.items(), key=lambda x: x[1])  # 获取出现最少的块编号

print(f"出现最多的块编号: {most_common_block[0]}, 出现次数: {most_common_block[1]}")
print(f"出现最少的块编号: {least_common_block[0]}, 出现次数: {least_common_block[1]}")

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(block_ids, counts, color='skyblue')
plt.xlabel('Block ID')
plt.ylabel('Count')
plt.title('Block ID Occurrences in the Log')
plt.xticks(rotation=90)  # 旋转 x 轴标签，以便更好地显示
plt.tight_layout()

# 显示图表
plt.show()
