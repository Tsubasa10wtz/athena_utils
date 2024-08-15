import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 读取文件内容
prefix = './txt'
name = 'v100/v100/resnet_imagenet_cache/3epoch'
# name = 'v100/cpu/vgg_mit_cache/1worker/3iter'
txt_path = os.path.join(prefix, name) + '.txt'
with open(txt_path, 'r') as file:
    lines = file.readlines()


x = 0
# 解析数据
data = []
for line in lines:
    if 18096 < x < 25380:
        parts = line.split(':')
        id = int(parts[0].strip())
        times = parts[1].split('-')
        start = float(times[0].strip())
        end = float(times[1].strip())
        data.append((id, start, end))
    x += 1
    # x += 1
    # if x == 18096:
    #     break


# data = []
# for line in lines:
#     parts = line.split(':')
#     id = int(parts[0].strip())
#     times = parts[1].split('-')
#     start = float(times[0].strip())
#     end = float(times[1].strip())
#     data.append((id, start, end))


# 提取区间
intervals = [(start, end) for _, start, end in data]

# 增大字体大小
plt.rcParams.update({'font.size': 14})

# 绘制区间
fig, ax = plt.subplots(figsize=(12, 8))

# 将每个区间绘制为一个矩形
for i, (start, end) in enumerate(intervals):
    rect = patches.Rectangle((start, i - 0.4), end - start, 0.8, edgecolor='blue', facecolor='cyan', alpha=0.5)
    ax.add_patch(rect)

# 设置图表的限制和标签
x_min = min(start for start, end in intervals)
x_max = max(end for start, end in intervals)


ax.set_xlim(x_min, x_max)
ax.set_ylim(-1, len(intervals))
ax.set_xlabel('Time(s)', fontsize=20)
ax.set_ylabel('IO Number', fontsize=20)
ax.set_title('IO Time Interval Distribution', fontsize=26)

# 增大刻度标签的字体大小
ax.tick_params(axis='both', which='major', labelsize=20)

# 保存图表为PDF格式
prefix = './pic'
save_path = os.path.join(prefix, name) + '.pdf'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='pdf')

# 显示图表
# plt.show()