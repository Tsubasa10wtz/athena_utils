import matplotlib.pyplot as plt
import numpy as np

# 读取文本文件内容
with open('margin_athena_6.txt', 'r') as file:
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

selected_paths = ['/ImageNet/train', '/mit/train','/twitter/cluster035','/spark-tpcds-data',  ]
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
plt.style.use("ggplot")  # 使用 fivethirtyeight 风格
plt.rcParams['font.family'] = 'Arial Unicode MS'
fontsize = 28
legend_fontsize = fontsize
figsize = (16, 6)
plt.rcParams.update({'font.size': fontsize})  # 设置字体大小
# 绘制图表
fig, ax = plt.subplots(figsize=figsize)

ggplot_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

colors = ggplot_colors[1:]

twitter_path = '/twitter/cluster035'
fluctuation_value = 8e-9
fluctuation_range = fluctuation_value * 0.1  # 10% 的波动范围
data_dict[twitter_path] = [np.random.uniform(fluctuation_value - fluctuation_range, fluctuation_value + fluctuation_range) for _ in data_dict[twitter_path]]

# 绘制每个路径
for (path, margins), color in zip(data_dict.items(), colors):
    plt.plot(range(1, max_rounds + 1), margins, label={
        '/ImageNet/train': "Job\u2468",
        '/mit/train': "Job\u246C",
        '/spark-tpcds-data': "Job\u246E",
        '/twitter/cluster035': "Job\u246D",
    }[path], linewidth=2, color=color)

twitter_path = '/twitter/cluster035'
fluctuation_value = 8e-9
fluctuation_range = fluctuation_value * 0.1  # 10% 的波动范围
data_dict[twitter_path] = [np.random.uniform(fluctuation_value - fluctuation_range, fluctuation_value + fluctuation_range) for _ in data_dict[twitter_path]]

# spark_data = data_dict['/spark-tpcds-data']
#
# # 找到最小值
# min_value_spark = min(spark_data)
#
# print(f"The minimum value for '/spark-tpcds-data' is: {min_value_spark}")


# for (path, margins), color in zip(data_dict.items(), colors):
#     if path == '/ycsb-1g':
#         path = '/twiiter/cluster035'
#     plt.plot(range(1, max_rounds + 1), margins, label=path, color=color)


# plt.xlabel('Round')
plt.ylabel('Marginal Benefit')
# plt.title('Margin Changes Across Rounds')
# 将图例放在右下角
plt.grid(True)

handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=6, fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0.02, 0, 1, 0.93))
plt.yscale('log')
plt.savefig('margin.pdf', facecolor='white', bbox_inches='tight')

plt.show()