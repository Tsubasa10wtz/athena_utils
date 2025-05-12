import matplotlib.pyplot as plt
from collections import Counter
import re

# 读取文件并提取Offset
offsets = []
with open('/Users/wangtianze/直博/项目/Athena/athena/plot/RAG/filtered_triviaqa_diskann_1221.txt', 'r') as file:
    for line in file:
        match = re.search(r'Offset:\s+(\d+)', line)
        if match:
            offsets.append(int(match.group(1)))

# 统计每个Offset的出现次数
offset_counts = Counter(offsets)

# 获取最高频的10个Offset
top_10 = offset_counts.most_common(10)
top_offsets = [f'{x[0]//4096}' for x in top_10]
top_counts = [x[1] for x in top_10]

# 获取最低频的10个Offset
bottom_10 = offset_counts.most_common()[-10:]
bottom_offsets = [f'{x[0]//4096}' for x in bottom_10]
bottom_counts = [x[1] for x in bottom_10]

# 创建图表
plt.figure(figsize=(14, 6))

# Top 10
plt.subplot(1, 2, 1)
bars_top = plt.bar(top_offsets, top_counts, color='skyblue', edgecolor='black', linewidth=1)
plt.title('Top 10 Frequent Indexes', fontsize=30)
plt.xlabel('Index', fontsize=26)
plt.ylabel('Occurrence Count', fontsize=26)
plt.xticks(rotation=45, fontsize=16)
plt.yticks(fontsize=16)
plt.ylim(0, 1000)

for bar in bars_top:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{height}', ha='center', va='bottom', fontsize=12)

# Bottom 10
plt.subplot(1, 2, 2)
bars_bottom = plt.bar(bottom_offsets, bottom_counts, color='lightcoral', edgecolor='black', linewidth=1)
plt.title('Bottom 10 Frequent Indexes', fontsize=30)
plt.xlabel('Index', fontsize=26)
plt.xticks(rotation=45, fontsize=16)
plt.yticks(fontsize=16)
plt.ylim(0, 10)

for bar in bars_bottom:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{height}', ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.show()
