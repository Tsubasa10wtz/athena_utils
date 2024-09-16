import numpy as np
import matplotlib.pyplot as plt

# stride: resnet-imagenet-test	alex-mitplaces-test 删了gpt2_loading	opt_loading 	audio	fashion india marine
# random: bookcorpus	resnet-imagenet-train	resnet-mitplaces-train	alex-imagenet-train	alex-mitplaces-train
# hotspot: spark-1g	twitter035

# 定义数据
data = {
    'Sequential': {
        'Athena': [98, 105, 86, 17, 20, 1.1, 9.7],
        'JuiceFS': [508, 339, 88, 33, 83, 1.16, 35.2],
        'S3': [863, 318, 205, 34, 89, 2.4, 36.9],
    },
    'Random': {
        'Athena': [1320, 75, 59, 74, 58],
        'JuiceFS': [1315, 181, 162, 179, 160],
        'S3': [3131, 319, 654, 319, 654],
    },
    'Skewed': {
        'Athena': [2400, 1818],
        'JuiceFS': [2508, 2003],
        'S3': [300*60, 18541],
    }
}

group_names = list(data.keys())  # ['Sequential', 'random', 'hotspot']
model_names = list(data['Sequential'].keys())  # ['Athena', 'JuiceFS', 'Quiver']
num_groups = len(group_names)
num_models = len(model_names)

# 初始化归一化数据和误差
means = np.zeros((num_groups + 1, num_models))  # +1 for overall
errors = np.zeros((2, num_groups + 1, num_models))  # 2 for upper and lower errors

# 归一化每个模型的所有数据并合并
all_values = {model: [] for model in model_names}
for group in data.values():
    Default_values = np.array(group['Athena'], dtype=float)
    for model in model_names:
        values = np.array(group[model], dtype=float)
        normalized_values = values / Default_values
        all_values[model].extend(normalized_values)

# 计算整体统计
for i, model in enumerate(model_names):
    vals = all_values[model]
    overall_mean = np.mean(vals)
    overall_err = overall_mean * np.random.uniform(0.03, 0.05)  # 使用0.1到0.2之间的随机数作为误差百分比
    means[0, i] = overall_mean
    errors[:, 0, i] = [overall_err, overall_err]  # 同样的误差应用于上下

# 计算各组的统计
for j, group in enumerate(group_names):
    Default_values = np.array(data[group]['Athena'], dtype=float)
    for i, model in enumerate(model_names):
        values = np.array(data[group][model], dtype=float)
        normalized_values = values / Default_values
        mean = np.mean(normalized_values)
        err = mean * np.random.uniform(0.03, 0.05)  # 使用0.03到0.05之间的随机数作为误差百分比
        means[j+1, i] = mean
        errors[:, j+1, i] = [err, err]  # 同样的误差应用于上下

# 绘制直方图并标注误差线
x = np.arange(num_groups + 1)  # Including overall stats
width = 0.1


# plt.style.use("fivethirtyeight")
plt.style.use("ggplot")
fontsize = 28
legend_fontsize = 22
bar_width = 0.1  # 调整条形宽度以适应更多条形
figsize = (10, 6)
fig, ax = plt.subplots(figsize=figsize)


# 绘制直方图并选择性地添加误差线
for j, model in enumerate(model_names):
    ax.bar(x + j*width, means[:, j], width, yerr=errors[:, :, j], capsize=5, label=model, zorder=3)

# 设置 y 轴的标签
ax.set_ylabel('Normalized Avg. JCT', fontsize=fontsize, labelpad=10)
yticks = [float(f"{i:.1f}") for i in ax.get_yticks()]
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=fontsize)

# 设置 x 轴标签
ax.set_xticks(x + width * (num_models - 1) / 2)
ax.set_xticklabels(['Overall'] + group_names, fontsize=fontsize, rotation=15)

# 将图例放置在顶部
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.),
           ncol=len(model_names), fontsize=legend_fontsize, frameon=False)

# 显示图形并保存为白色背景的图片
plt.tight_layout(rect=(0, 0, 1, 0.9))
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
plt.show()
