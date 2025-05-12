import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random
from matplotlib import ticker  # 导入 ticker 模块

# 文件参数
total_size = 11 * 1024 ** 3  # 11GB
chunk_size = 131072  # 128KB
num_chunks = total_size // chunk_size  # 总块数

# 模拟3个epoch的随机访问
all_accessed = []
for epoch in range(3):
    chunks = list(range(num_chunks))
    random.shuffle(chunks)
    all_accessed.extend(chunks)

# 统计访问次数，并转换为Offset表示
chunk_counts = Counter(all_accessed)
offset_counts = {offset * chunk_size: count for offset, count in chunk_counts.items()}

# 获取访问最多和最少的10个Offset
top_10 = Counter(offset_counts).most_common(10)
bottom_10 = Counter(offset_counts).most_common()[-10:]

# 准备绘图数据（格式化Offset显示）
top_offsets = [f"{x[0]:,}" for x in top_10]
top_counts = [x[1] for x in top_10]
bottom_offsets = [f"{x[0]:,}" for x in bottom_10]
bottom_counts = [x[1] for x in bottom_10]

# 创建图表
plt.figure(figsize=(18, 6))

# --------------------------
# 高频访问Offset（左侧子图）
# --------------------------
plt.subplot(1, 2, 1)
bars_top = plt.bar(top_offsets, top_counts, color='skyblue')

plt.title('Top 10 Frequent Offsets', fontsize=30)
plt.xlabel('Offset', fontsize=26)
plt.ylabel('Occurrence Count', fontsize=26)
plt.xticks(rotation=45, fontsize=16)

# 设置y轴刻度间隔为1
ax = plt.gca()  # 获取当前坐标轴
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))  # 每1个单位一个刻度
plt.yticks(fontsize=16)
plt.ylim(0, 4)  # 稍微扩展上边界

# 添加柱状图数值标签
for bar in bars_top:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{height}', ha='center', va='bottom', fontsize=12)

# --------------------------
# 低频访问Offset（右侧子图）
# --------------------------
plt.subplot(1, 2, 2)
bars_bottom = plt.bar(bottom_offsets, bottom_counts, color='lightcoral')

plt.title('Bottom 10 Frequent Offsets', fontsize=30)
plt.xlabel('Offset', fontsize=26)
plt.ylabel('Occurrence Count', fontsize=26)
plt.xticks(rotation=45, fontsize=16)

# 设置y轴刻度间隔为1
ax = plt.gca()  # 获取当前坐标轴
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))  # 每1个单位一个刻度
plt.yticks(fontsize=16)
plt.ylim(0, 4)  # 固定范围0-10

# 添加柱状图数值标签
for bar in bars_bottom:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{height}', ha='center', va='bottom', fontsize=12)

# 调整布局并显示
plt.tight_layout()
plt.show()