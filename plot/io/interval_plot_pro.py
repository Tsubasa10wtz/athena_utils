import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 读取文件内容
prefix = './txt'
name = 'v100/v100/resnet_imagenet_cache/1worker/3iter'
# name = 'v100/cpu/resnet_imagenet_cache/1worker/3iter'
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

# 增大字体大小
plt.rcParams.update({'font.size': 24})

# 绘制区间
fig, ax = plt.subplots(figsize=(12, 8))

# 将每个区间绘制为一个矩形
for i, (start, end) in enumerate(intervals):
    rect = patches.Rectangle((start, i - 0.4), end - start, 0.8, edgecolor='blue', facecolor='cyan', alpha=0.5)
    ax.add_patch(rect)

# 设置图表的限制和标签
x_min = min(start for start, end in intervals) - 0.01
x_max = max(end for start, end in intervals) + 0.01

ax.set_xlim(x_min, x_max)
ax.set_ylim(-1, len(intervals))
ax.set_xlabel('Time(s)')
ax.set_ylabel('IO Number')
# ax.set_title('IO Time Interval Distribution')

# 增大刻度标签的字体大小
ax.tick_params(axis='both', which='major')

# 保存图表为PDF格式
prefix = './pic'
save_path = os.path.join(prefix, name) + '.pdf'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='pdf')


# 显示图表
plt.show()
