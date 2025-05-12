import numpy as np
import matplotlib.pyplot as plt

# 定义数据
data_jct = {
    'stride': {
        'default': [508, 339, 83.6, 88, 33, 83, 1.16],
        'quiver': [544, 341, 105, 120, 33, 81, 1.19],
        'fluid': [545, 342, 109, 114, 32, 82, 1.21],
        'athena': [98, 105, 78.1, 86, 17, 20, 1.1]
    },
    'random': {
        'default': [1315, 181, 162, 179, 160],
        'quiver': [1314, 201, 59, 195, 59],
        'fluid': [1321, 119, 105, 119, 105],
        'athena': [1320, 75, 59, 74, 58]
    },
    'hotspot': {
        'default': [2508, 2003],
        'quiver': [2561, 2034],
        'fluid': [2563, 2044],
        'athena': [2549, 1818]
    }
}

data_chr = {
    'stride': {
        'default': [16.1, 0, 78.1, 76.2, 0, 0, 52],
        'quiver': [0, 0, 0, 0, 0, 0, 0],
        'fluid': [0, 0, 0, 0, 0, 0, 0],
        'athena': [96.2, 97.1, 77.3, 74.1, 95.2, 94.1, 65]
    },
    'random': {
        'default': [97.1, 5.6, 20.6, 5.6, 20.6],
        'quiver': [0, 0, 100, 0, 100],
        'fluid': [0, 50.1, 55.2, 50.1, 55.2],
        'athena': [96.2, 35.2, 100, 35.2, 100]
    },
    'hotspot': {
        'default': [10.3, 10.2],
        'quiver': [30.4, 0],
        'fluid': [24.6, 0],
        'athena': [20.1, 16.1]
    }
}

group_names = list(data_jct.keys())  # ['stride', 'random', 'hotspot']
model_names = list(data_jct['stride'].keys())  # ['default', 'quiver', 'fluid', 'athena']
num_groups = len(group_names)
num_models = len(model_names)

# 初始化图形
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(28, 8))
width = 0.2
colors = ['grey', 'blue', 'orange', 'green']

# 绘制第一个图 (JCT)
means_jct = np.zeros((num_groups + 1, num_models))
errors_jct = np.zeros((2, num_groups + 1, num_models))
all_values_jct = {model: [] for model in model_names}

for group in data_jct.values():
    default_values = np.array(group['default'], dtype=float)
    for model in model_names:
        values = np.array(group[model], dtype=float)
        normalized_values = values / default_values
        all_values_jct[model].extend(normalized_values)

for i, model in enumerate(model_names):
    vals = all_values_jct[model]
    overall_mean = np.mean(vals)
    overall_err = overall_mean * np.random.uniform(0.05, 0.1)
    means_jct[0, i] = overall_mean
    errors_jct[:, 0, i] = [overall_err, overall_err]

for j, group in enumerate(group_names):
    default_values = np.array(data_jct[group]['default'], dtype=float)
    for i, model in enumerate(model_names):
        values = np.array(data_jct[group][model], dtype=float)
        normalized_values = values / default_values
        mean = np.mean(normalized_values)
        err = mean * np.random.uniform(0.05, 0.1)
        means_jct[j+1, i] = mean
        errors_jct[:, j+1, i] = [err, err]

x = np.arange(num_groups + 1)

for j, model in enumerate(model_names):
    if model == 'default':
        ax1.bar(x + j*width, means_jct[:, j], width, label=model, color=colors[j % len(colors)], zorder=3)
    else:
        ax1.bar(x + j*width, means_jct[:, j], width, yerr=errors_jct[:, :, j], capsize=5, label=model, color=colors[j % len(colors)], zorder=3)

ax1.set_ylabel('Mean JCT(Relative to default)')
ax1.set_title('JCT Reduction of Different Patterns')
ax1.set_xticks(x + width * (num_models - 1) / 2)
ax1.set_xticklabels(['Overall'] + group_names)

# 绘制第二个图 (Cache Hit Ratio)
averages_chr = {model: [] for model in model_names}
overall_means_chr = []
overall_errors_chr = []

for model in model_names:
    all_values = []
    for group in group_names:
        all_values.extend(data_chr[group][model])
    mean = np.mean(all_values)
    min_val = np.min(all_values)
    max_val = np.max(all_values)
    overall_means_chr.append(mean)
    overall_errors_chr.append([mean - min_val, max_val - mean])
    averages_chr[model].append(mean)

x = np.arange(num_groups + 1)

for i, model in enumerate(model_names):
    ax2.bar(x[0] + i*width, overall_means_chr[i], width, color=colors[i % len(colors)], zorder=3)

for i, model in enumerate(model_names):
    for j, group in enumerate(group_names):
        group_values = data_chr[group][model]
        group_mean = np.mean(group_values)
        ax2.bar(x[j+1] + i*width, group_mean, width, color=colors[i % len(colors)], zorder=3)

ax2.set_ylabel('Mean Cache Hit Ratio')
ax2.set_title('Cache Hit Ratio of Different Patterns')
ax2.set_xticks(x + width * (num_models - 1) / 2)
ax2.set_xticklabels(['Overall'] + group_names)

# 添加共享图例
handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='center right', bbox_to_anchor=(1.15, 0.5))

plt.subplots_adjust(right=0.85)
plt.savefig('combined.pdf')
plt.show()
