import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import ticker

# 读取文件内容
prefix = './txt'
name = 'v100/cpu/resnet_imagenet_cache/1worker/3iter'
txt_path = os.path.join(prefix, name) + '.txt'
with open(txt_path, 'r') as file:
    lines = file.readlines()

data = []
for line in lines:
    parts = line.split(':')
    id = int(parts[0].strip())
    times = parts[1].split('-')
    start = float(times[0].strip())
    end = float(times[1].strip())
    data.append((id, start, end))

# 提取区间，并调整时间轴
start_time = data[0][1]
intervals = [(start - start_time, end - start_time) for _, start, end in data]

plt.style.use("ggplot")
# 增大字体大小
plt.rcParams.update({'font.size': 30})

# 绘制区间
fig, ax = plt.subplots(figsize=(8, 7))

# 将每个区间绘制为一个矩形
for i, (start, end) in enumerate(intervals):
    rect = patches.Rectangle((start, i - 0.4), end - start, 0.8, edgecolor='blue')
    ax.add_patch(rect)

# 设置图表的限制和标签
x_min = min(start for start, end in intervals) - 0.01
x_max = max(end for start, end in intervals) + 0.01

print(len(intervals))

ax.set_xlim(x_min, x_max)
ax.set_ylim(-1, 280)
ax.set_xlabel('Time(s)')
ax.set_ylabel('IO Request Ordinal')
ax.set_xlim(0, 12.2)

# 增大刻度标签的字体大小
ax.tick_params(axis='both', which='major')

## 添加其他图形

rect1 = patches.Rectangle((0.05, 0), 0.90, 96, edgecolor='red', facecolor='none', linewidth=2)
ax.add_patch(rect1)

rect2 = patches.Rectangle((4.8, 96), 0.85, 90, edgecolor='red', facecolor='none', linewidth=2)
ax.add_patch(rect2)

rect3 = patches.Rectangle((9.6, 186), 0.78, 91, edgecolor='red', facecolor='none', linewidth=2)
ax.add_patch(rect3)




# 创建文本
# ax.text(0.4, 103, 'Batch I/O', fontsize=24, color='red', fontweight='bold',
#         horizontalalignment='center', verticalalignment='center')

ax.text(5.25, 196, 'Batch I/O', fontsize=24, color='red', fontweight='bold',
        horizontalalignment='center', verticalalignment='center')

# ax.text(10, 179, 'Batch I/O', fontsize=24, color='red', fontweight='bold',
#         horizontalalignment='center', verticalalignment='center')

# 创建 FancyArrowPatch (起点, 终点)
arrow1 = patches.FancyArrowPatch((0, 120), (4.8, 120), color='green', linewidth=2, arrowstyle='<->', mutation_scale=20)
# 添加箭头到坐标轴
ax.add_patch(arrow1)

# ax.text(2.4, 127, 'Batch Computation', fontsize=24, color='green', fontweight='bold',
#         horizontalalignment='center', verticalalignment='center')

# 创建 FancyArrowPatch (起点, 终点)
arrow2 = patches.FancyArrowPatch((4.8, 210), (9.6, 210), color='green', linewidth=2, arrowstyle='<->', mutation_scale=20)
# 添加箭头到坐标轴
ax.add_patch(arrow2)

ax.text(7.2, 232, 'Batch\nComputation', fontsize=24, color='green', fontweight='bold',
        horizontalalignment='center', verticalalignment='center')

# # 创建 FancyArrowPatch (起点, 终点)
# arrow3 = patches.FancyArrowPatch((0.93, 96), (4.8, 96), color='orange', linewidth=2, arrowstyle='<->', mutation_scale=20)
# # 添加箭头到坐标轴
# ax.add_patch(arrow3)
#
# # 创建 FancyArrowPatch (起点, 终点)
# arrow4 = patches.FancyArrowPatch((5.65, 186), (9.6, 186), color='orange', linewidth=2, arrowstyle='<->', mutation_scale=20)
# # 添加箭头到坐标轴
# ax.add_patch(arrow4)

plt.tight_layout(rect=(-0.04, -0.04, 1.04, 1.04))
plt.savefig("paper/new_computation_bottleneck.pdf", format='pdf')

# 显示图表
plt.show()
