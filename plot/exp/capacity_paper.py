import matplotlib.pyplot as plt
import numpy as np

# 读取文本文件内容
with open('margin_athena_4.txt', 'r') as file:
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
selected_paths = ['/ycsb-1g', '/spark-tpcds-data', '/ImageNet/train', '/mit/train']
capacity_data_dict = {path: capacity_data_dict[path] for path in selected_paths if path in capacity_data_dict}

# 创建颜色映射
cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0, 1, len(capacity_data_dict)))

# 确保所有路径的数据长度相同
max_rounds = max(max(capacities, key=lambda x: x[0])[0] for capacities in capacity_data_dict.values())
for path in capacity_data_dict:
    round_capacities = capacity_data_dict[path]
    round_dict = {round_num: capacity for round_num, capacity in round_capacities}
    capacity_data_dict[path] = [round_dict.get(round_num, 0) for round_num in range(1, max_rounds + 1)]

plt.style.use("fivethirtyeight")  # 使用 fivethirtyeight 风格
plt.rcParams['font.family'] = 'Arial Unicode MS'

fontsize = 28
legend_fontsize = fontsize
figsize = (16, 6)
plt.rcParams.update({'font.size': fontsize})  # 设置字体大小
# 绘制图表
fig, ax = plt.subplots(figsize=figsize)

for (path, capacities), color in zip(capacity_data_dict.items(), colors):
    if path == '/ycsb-1g':
        path = '/twitter/cluster035'
    plt.plot(range(1, max_rounds + 1), capacities, label={
        '/twitter/cluster035': 'Twitter',
        '/spark-tpcds-data': "TPC-DS",
        '/ImageNet/train': "ImageNet",
        '/mit/train': "MITPlaces",
    }[path], linewidth=2, color=color)

plt.xlabel('Round')
plt.ylabel('Capacity (MB)')
# plt.title('Capacity Changes Across Rounds in MB')
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.grid(True)
# ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
# fig.patch.set_facecolor('white')  # 设置整个图形的背景
plt.savefig('capacity.pdf', facecolor='white', bbox_inches='tight')
plt.show()
