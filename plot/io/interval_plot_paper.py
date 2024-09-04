import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 读取文件内容
prefix = './txt'
name = 'v100/v100/resnet_imagenet_cache/1worker/3iter'
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
plt.rcParams.update({'font.size': 26})

# 绘制区间
fig, ax = plt.subplots(figsize=(10, 8))

# 将每个区间绘制为一个矩形
for i, (start, end) in enumerate(intervals):
    rect = patches.Rectangle((start, i - 0.4), end - start, 0.8, edgecolor='blue')
    ax.add_patch(rect)

# 设置图表的限制和标签
x_min = min(start for start, end in intervals) - 0.01
x_max = max(end for start, end in intervals) + 0.01

ax.set_xlim(x_min, x_max)
ax.set_ylim(-1, len(intervals))
ax.set_xlabel('Time(s)')
ax.set_ylabel('IO Request Ordinal')

# 增大刻度标签的字体大小
ax.tick_params(axis='both', which='major')

# 增加局部放大的区域
# 设定 y 轴的放大范围
y_min, y_max = 25, 30

# 自动确定放大区域的 x 轴范围
zoom_start = float('inf')
zoom_end = float('-inf')

for i, (start, end) in enumerate(intervals):
    if y_min <= i <= y_max:
        zoom_start = min(zoom_start, start)
        zoom_end = max(zoom_end, end)

# 如果找到合适的区域，则进行放大显示
if zoom_start < zoom_end:
    # 创建嵌套的放大轴
    ax_inset = ax.inset_axes([0.3, 0.1, 0.2, 0.2])  # 位置参数 [left, bottom, width, height]

    # 在嵌套轴中绘制放大的矩形区域
    for i, (start, end) in enumerate(intervals):
        if y_min <= i <= y_max:
            rect = patches.Rectangle((start, i - 0.4), end - start, 0.8, edgecolor='blue')
            ax_inset.add_patch(rect)

    # 设置放大区域的 x 和 y 轴范围
    ax_inset.set_xlim(zoom_start, zoom_end)
    ax_inset.set_ylim(y_min - 1, y_max + 1)
    # ax_inset.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax_inset.grid(False)

    # 在主图上标记出放大区域
    # ax.indicate_inset_zoom(ax_inset, linewidth=1, linestyle="-", alpha=1)

    for spine in ax_inset.spines.values():
        spine.set_linewidth(2)  # 设置放大框的线宽

## 添加其他图形

rect1 = patches.Rectangle((0, 0), 0.5, 80, edgecolor='red', facecolor='none', linewidth=2)
ax.add_patch(rect1)


plt.tight_layout()

# 显示图表
plt.show()
