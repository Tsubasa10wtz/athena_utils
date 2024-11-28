import numpy as np
import matplotlib.pyplot as plt

# 定义数据，只保留JuiceFS和Athena
data = {
    'Sequential': {
        'Athena': [96.2, 97.1, 74.1, 95.2, 94.1, 65, 99],
        'JuiceFS': [16.1, 0, 76.2, 0, 0, 52, 0],
    },
    'Random': {
        'Athena': [96.2, 35.2, 100, 35.2, 100],
        'JuiceFS': [97.1, 5.6, 20.6, 5.6, 20.6],
    },
    'Skewed': {
        'Athena': [70.1, 88.2],
        'JuiceFS': [60.3, 70.2],
    }
}

group_names = list(data.keys())  # ['Sequential', 'Random', 'Skewed']
model_names = ['Athena', 'JuiceFS']  # 只保留Athena和JuiceFS
num_groups = len(group_names)
num_models = len(model_names)

# 计算总体统计
averages = {model: [] for model in model_names}
overall_means = []
overall_errors = []
for model in model_names:
    all_values = []
    for group in group_names:
        all_values.extend(data[group][model])
    mean = np.mean(all_values)
    min_val = np.min(all_values)
    max_val = np.max(all_values)
    overall_means.append(mean)
    overall_errors.append([mean - min_val, max_val - mean])  # Errors as [lower, upper]
    averages[model].append(mean)  # Append overall average for first cluster

# 绘制直方图
x = np.arange(num_groups + 1)  # Including overall stats
width = 0.1  # the width of the bars

plt.style.use("ggplot")
fontsize = 28
legend_fontsize = 22
bar_width = 0.1  # 调整条形宽度以适应更多条形
figsize = (10, 6)
fig, ax = plt.subplots(figsize=figsize)

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# First, draw the overall stats
for i, model in enumerate(model_names):
    ax.bar(x[0] + i*width, overall_means[i], width, capsize=5, label=model, color=colors[i % len(colors)], zorder=3)

# Then draw each group
for i, model in enumerate(model_names):
    for j, group in enumerate(group_names):
        group_values = data[group][model]
        group_mean = np.mean(group_values)
        group_min = np.min(group_values)
        group_max = np.max(group_values)
        ax.bar(x[j+1] + i*width, group_mean, width, capsize=5, color=colors[i % len(colors)], zorder=3)

ax.set_ylabel('Avg. CHR (%)', fontsize=fontsize)
yticks = [int(i) for i in ax.get_yticks()]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

ax.set_xticks(x + width * (num_models - 1) / 2)
ax.set_xticklabels(['Overall'] + group_names, fontsize=fontsize, rotation=15)
plt.subplots_adjust(top=0.8)

# 将图例放置在顶部
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=len(model_names), fontsize=legend_fontsize, frameon=False)

plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('chr.pdf', facecolor='white', bbox_inches='tight')
plt.show()
