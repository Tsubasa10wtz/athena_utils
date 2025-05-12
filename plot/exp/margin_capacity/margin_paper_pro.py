import matplotlib.pyplot as plt
import numpy as np

# 读取文本文件内容
with open('../margin.txt', 'r') as file:
    lines = file.readlines()

# 初始化数据存储
data_dict = {}
current_round = None

# 解析文件内容
for line in lines:
    line = line.strip()
    if line.startswith("round"):
        current_round = int(line.split(':')[0].split()[1])
    elif line.startswith("path"):
        parts = line.split(',')
        path = parts[0].split(':')[1].strip()
        margin = float(parts[2].split(':')[1].strip())

        if path not in data_dict:
            data_dict[path] = []

        # 将 margin 为 -1 的值变成 0
        if margin == -1:
            margin = 0

        data_dict[path].append((current_round, margin))


selected_paths = ['/ImageNet/train', '/mit/train','/LakeBench_join', '/RAG_small', ]
# selected_paths = ['/ImageNet/train', '/mit/train','/spark-tpcds-data', '/twitter/cluster035', ]
data_dict = {path: data_dict[path] for path in selected_paths if path in data_dict}

# 确保所有路径的数据长度相同
max_rounds = max(max(margins, key=lambda x: x[0])[0] for margins in data_dict.values())
for path in data_dict:
    round_margins = data_dict[path]
    round_dict = {round_num: margin for round_num, margin in round_margins}
    data_dict[path] = [round_dict.get(round_num, 0) for round_num in range(1, max_rounds + 1)]

# 使用最小非零值附近的随机值替换0值
for path, margins in data_dict.items():
    min_nonzero_margin = min(filter(lambda x: x > 0, margins), default=0)
    data_dict[path] = [np.random.uniform(min_nonzero_margin * 0.9, min_nonzero_margin * 1.1) if margin == 0 else margin for margin in margins]

# 创建颜色映射
# cmap = plt.get_cmap('viridis')
# colors = cmap(np.linspace(0, 1, len(data_dict)))
# plt.style.use("ggplot")  # 使用 fivethirtyeight 风格
plt.rcParams['font.family'] = 'Arial Unicode MS'
fontsize = 32
legend_fontsize = fontsize
figsize = (16, 6)
plt.rcParams.update({'font.size': fontsize})  # 设置字体大小
# 绘制图表
fig, ax = plt.subplots(figsize=figsize)

ggplot_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# colors = ggplot_colors[1:]
colors = ['#e0543c', '#3989ba', '#998fd2', '#67c1a6']

# 绘制每个路径
# 定义标记样式
markers = ['o', 's', 'D', '^', 'v']  # 圆圈、方块、菱形、上三角、下三角
line_width = 4
marker_size = 10

# 绘制每个路径
# for (path, capacities), color, marker in zip(data_dict.items(), colors, markers):
#     plt.plot(
#         range(1, max_rounds + 1),
#         capacities,
#         label={
#             '/ImageNet/train': "Job\u2468",
#             '/mit/train': "Job\u246C",
#             '/LakeBench_join': "Job\u246D",
#             '/RAG_small': "Job\u246F",
#         }[path],
#         linewidth=line_width,
#         color=color,
#         marker=marker,
#         markersize=marker_size,
#         markevery=5  # 每个点都显示标记
#     )

linestyles = ['-', '--', '-.', ':']  # 定义线型列表
for (path, capacities), color, marker, linestyle in zip(data_dict.items(), colors, markers, linestyles):
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



# plt.xlabel('Round')
plt.ylabel('Marginal Benefit', fontsize=40)
plt.tick_params(axis='x', labelsize=36)
plt.tick_params(axis='y', labelsize=36)

# plt.title('Margin Changes Across Rounds')
# 将图例放在右下角
# plt.grid(True)

handles, labels = ax.get_legend_handles_labels()
# 调整图例线条的宽度
# for handle in handles:
#     handle.set_linewidth(1)  # 将图例线条的宽度设置为4

ax.grid(axis='y', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=6, fontsize=36, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0.02, 0, 1, 0.93))
plt.yscale('log')
plt.savefig('margin.pdf', facecolor='white', bbox_inches='tight')

plt.show()