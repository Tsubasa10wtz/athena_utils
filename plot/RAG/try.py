import matplotlib.pyplot as plt
from collections import Counter

# 读取 filtered_log.txt 文件
with open('filtered_log.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# 用于存储每个块编号的计数
block_counts = Counter()

# 提取所有 Offset 值并计算最小和最大 Offset
offsets = []

# 处理每一行，提取 Offset，计算块编号
for line in lines:
    # 找到 "Offset:" 后的数值
    parts = line.split(',')
    for part in parts:
        if "Offset:" in part:
            offset_str = part.split(':')[1].strip()
            offset = int(offset_str)  # 转换为整数
            offsets.append(offset)

# 计算最小和最大 Offset
min_offset = min(offsets)
max_offset = max(offsets)

# 根据最小和最大 Offset 计算块编号范围
block_range = range(min_offset // (4 * 1024 * 1024), max_offset // (4 * 1024 * 1024) + 1)  # 注意加1

# 处理每一行，提取 Offset，计算块编号并统计出现次数
for offset in offsets:
    # 计算块编号
    block_id = offset // (4 * 1024 * 1024)  # 除以 4MB
    block_counts[block_id] += 1

# 包含所有块编号，即使出现次数为 0
for block_id in block_range:
    if block_id not in block_counts:
        block_counts[block_id] = 0

# # 按照块编号（key）对 block_counts 进行排序
# sorted_block_counts = sorted(block_counts.items())
#
# print(len(sorted_block_counts))
#
# # 输出排序后的块编号和出现次数
# for block_id, count in sorted_block_counts:
#     print(f"块编号: {block_id}, 出现次数: {count}")


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
plt.bar(block_ids, counts, color='skyblue', width=0.5)
plt.xlabel('Block ID')
plt.ylabel('Count')
plt.title('Block ID Occurrences in the Log')
plt.xticks(rotation=90)  # 旋转 x 轴标签，以便更好地显示
plt.tight_layout()

# 保存图表为 PDF 文件
plt.savefig('block_counts_plot.pdf', format='pdf')

# 关闭图形，以释放资源
plt.close()
