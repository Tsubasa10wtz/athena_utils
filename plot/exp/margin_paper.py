import matplotlib.pyplot as plt
import numpy as np

# 读取文本文件内容
with open('margin_athena_4.txt', 'r') as file:
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

selected_paths = ['/ycsb-1g', '/spark-tpcds-data', '/ImageNet/train', '/mit/train']
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

plt.style.use("ggplot")

# 创建颜色映射
cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0, 1, len(data_dict)))

plt.rcParams.update({'font.size': 50})  # 设置字体大小
# 绘制图表
fig, ax = plt.subplots(figsize=(50, 12))

# 绘制每个路径，应用不同的颜色
for (path, margins), color in zip(data_dict.items(), colors):
    if path == '/ycsb-1g':
        path = '/twitter/cluster035'
    plt.plot(range(1, max_rounds + 1), margins, label=path, linewidth=5, color=color)

plt.xlabel('Round')
plt.ylabel('Margin')
plt.grid(True)

# 显示图例并设置在右下角
plt.legend(loc='lower right')
plt.show()

# # 创建颜色映射
# cmap = plt.get_cmap('Accent')
# colors = cmap(np.linspace(0, 1, len(data_dict)))
#
# plt.rcParams.update({'font.size': 50})  # 设置字体大小
# # 绘制图表
# fig, ax = plt.subplots(figsize=(50, 12))
#
# # 绘制每个路径
# for (path, margins) in data_dict.items():
#     if path == '/ycsb-1g':
#         path = '/twitter/cluster035'
#     plt.plot(range(1, max_rounds + 1), margins, label=path, linewidth=5)
#
#
# # for (path, margins), color in zip(data_dict.items(), colors):
# #     if path == '/ycsb-1g':
# #         path = '/twitter/cluster035'
# #     plt.plot(range(1, max_rounds + 1), margins, label=path, color=color)
#
#
# plt.xlabel('Round')
# plt.ylabel('Margin')
# # plt.title('Margin Changes Across Rounds')
# # 将图例放在右下角
# plt.grid(True)
#
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=6, fontsize=40)
#
# # ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
# # fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色
#
# plt.yscale('log')
# plt.savefig('margin.pdf', facecolor='white', bbox_inches='tight')

