import matplotlib.pyplot as plt
import numpy as np

# 读取文本文件内容
with open('../margin.txt', 'r') as file:
    lines = file.readlines()

# 初始化数据存储
capacity_data_dict = {}
current_round = None

# 解析文件内容
for line in lines:
    line = line.strip()
    if line.startswith("round"):
        current_round = int(line.split(':')[0].split()[1])
    elif line.startswith("path"):
        parts = line.split(',')
        path = parts[0].split(':')[1].strip()
        capacity = float(parts[1].split(':')[1].strip())

        if path not in capacity_data_dict:
            capacity_data_dict[path] = []

        # 将capacity除以1024*1024，转换为MB
        capacity /= (1024 * 1024)

        capacity_data_dict[path].append((current_round, capacity))

# 只选择特定的路径
# selected_paths = ['/ImageNet/train', '/mit/train','/spark-tpcds-data','/twitter/cluster035',  ]
selected_paths = ['/ImageNet/train', '/mit/train','/LakeBench_join', '/RAG_small', ]
capacity_data_dict = {path: capacity_data_dict[path] for path in selected_paths if path in capacity_data_dict}

# 确保所有路径的数据长度相同
max_rounds = max(max(capacities, key=lambda x: x[0])[0] for capacities in capacity_data_dict.values())
for path in capacity_data_dict:
    round_capacities = capacity_data_dict[path]
    round_dict = {round_num: capacity for round_num, capacity in round_capacities}
    capacity_data_dict[path] = [round_dict.get(round_num, 0) for round_num in range(1, max_rounds + 1)]

# if '/ImageNet/train' in capacity_data_dict:
#     capacity_data_dict['/ImageNet/train'] = [capacity - 250 for capacity in capacity_data_dict['/ImageNet/train']]

# 给所有值 *10，然后转换为GB（MB除以1024）
for path in capacity_data_dict:
    capacity_data_dict[path] = [(capacity * 10) / 1024 for capacity in capacity_data_dict[path]]


# 创建颜色映射
# cmap = plt.get_cmap('rainbow')
# colors = cmap(np.linspace(0, 1, len(capacity_data_dict)))

# plt.style.use("ggplot")  # 使用 fivethirtyeight 风格
plt.rcParams['font.family'] = 'Arial Unicode MS'

fontsize = 32
legend_fontsize = fontsize
figsize = (16, 6)
plt.rcParams.update({'font.size': fontsize})  # 设置字体大小
# 绘制图表
fig, ax = plt.subplots(figsize=figsize)

# rgb_colors = [
#     (180, 227, 211),    # 红色
#     (150, 187, 213),    # 绿色
#     (168, 192, 254),    # 蓝色
#     (222, 174, 127)   # 橙色
# ]
#
# colors = [(r/255, g/255, b/255) for r, g, b in rgb_colors]

ggplot_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

colors = ['#e0543c', '#3989ba', '#998fd2', '#67c1a6']

# colors = ['Purples', 'Blues', 'Greens', 'Oranges']


markers = ['o', 's', 'D', '^', 'v']  # 圆圈、方块、菱形、上三角、下三角
line_width = 4  # 线条宽度
marker_size = 8  # 标记大小
#
# 绘制每个路径
# for (path, capacities), color, marker in zip(capacity_data_dict.items(), colors, markers):
#     plt.plot(
#         range(1, max_rounds + 1),  # x 轴数据
#         capacities,  # y 轴数据
#         label={
#             '/ImageNet/train': "Job\u2468",
#             '/mit/train': "Job\u246C",
#             '/LakeBench_join': "Job\u246D",
#             '/RAG_small': "Job\u246F",
#         }[path],  # 图例标签
#         linewidth=line_width,  # 线条粗细
#         color=color,  # 线条颜色
#         marker=marker,  # 标记样式
#         markersize=marker_size,  # 标记大小
#         markevery=3  # 每个数据点显示标记
#     )

linestyles = ['-', '--', '-.', ':']  # 定义线型列表
for (path, capacities), color, marker, linestyle in zip(capacity_data_dict.items(), colors, markers, linestyles):
    plt.plot(
        range(1, max_rounds + 1),
        capacities,
        label={
            '/ImageNet/train': "Job\u2468",
            '/mit/train': "Job\u246C",
            '/LakeBench_join': "Job\u246D",
            '/RAG_small': "Job\u246F",
        }[path],
        linewidth=line_width,
        color=color,


        linestyle=linestyle,  # 添加线型

    )



plt.xlabel('Round',fontsize=40)
plt.ylabel('Capacity (GB)',labelpad=45,fontsize=40)

plt.tick_params(axis='x', labelsize=36)
plt.tick_params(axis='y', labelsize=36)

ax.set_ylim(0, 4.5)
ax.set_yticks(np.arange(0, 5, 1))

ax.grid(axis='y', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
# plt.title('Capacity Changes Across Rounds in GB')
handles, labels = ax.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
#            ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0.04, 0, 1, 0.93))
# plt.grid(True)
# ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
# fig.patch.set_facecolor('white')  # 设置整个图形的背景
plt.savefig('capacity.pdf', facecolor='white', bbox_inches='tight')
plt.show()
