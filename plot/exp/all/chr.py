import numpy as np
import matplotlib.pyplot as plt

# stride: resnet-imagenet-test	alex-mitpalces-test gpt2_loading	opt_loading 	audio	fashion 	india
# random: bookcorpus	resnet-imagenet-train	resnet-mitplaces-train	alex-imagenet-train	alex-mitplaces-train
# hotspot: spark-1g	ycsb

# 定义数据
data = {
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

group_names = list(data.keys())  # ['stride', 'random', 'hotspot']
model_names = list(data['stride'].keys())  # ['default', 'quiver', 'fluid', 'athena']
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
width = 0.2  # the width of the bars

plt.style.use("bmh")
plt.rcParams.update({'font.size': 24})

fig, ax = plt.subplots(figsize=(14, 8))


colors = ['grey', 'blue', 'orange', 'green']

# First, draw the overall stats
for i, model in enumerate(model_names):
    # ax.bar(x[0] + i*width, overall_means[i], width, yerr=np.array(overall_errors[i]).reshape(2, 1), capsize=5, label=model, color=colors[i % len(colors)],zorder=3)
    ax.bar(x[0] + i*width, overall_means[i], width, capsize=5, label=model, color=colors[i % len(colors)],zorder=3)

# Then draw each group
for i, model in enumerate(model_names):
    for j, group in enumerate(group_names):
        group_values = data[group][model]
        group_mean = np.mean(group_values)
        group_min = np.min(group_values)
        group_max = np.max(group_values)
        ax.bar(x[j+1] + i*width, group_mean, width, capsize=5, color=colors[i % len(colors)],zorder=3)

ax.set_ylabel('Mean Cache Hit Ratio')
ax.set_title('Cache Hit Ratio of Different Patterns')
ax.set_xticks(x + width * (num_models - 1) / 2)
ax.set_xticklabels(['Overall'] + group_names)
plt.subplots_adjust(right=0.8)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.show()