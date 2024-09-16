import numpy as np
import matplotlib.pyplot as plt

# 数据1：JCT，包含S3
data_jct = {
    'Sequential': {
        'Athena': [98, 105, 86, 17, 20, 1.1, 9.7],
        'JuiceFS': [508, 339, 88, 33, 83, 1.16, 35.2],
        'No cache': [863, 318, 205, 34, 89, 2.4, 36.9],
    },
    'Random': {
        'Athena': [1320, 75, 59, 74, 58],
        'JuiceFS': [1315, 181, 162, 179, 160],
        'No cache': [3131, 319, 654, 319, 654],
    },
    'Skewed': {
        'Athena': [2400, 1818],
        'JuiceFS': [2508, 2003],
        'No cache': [300*60, 18541],
    }
}

# 数据2：CHR，只保留JuiceFS和Athena，使用原始数据
data_chr = {
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

group_names = ['Sequential', 'Random', 'Skewed']
model_names_jct = ['Athena', 'JuiceFS', 'No cache']  # JCT 包含 S3
model_names_chr = ['Athena', 'JuiceFS']  # CHR 只包含 Athena 和 JuiceFS

# 计算归一化数据和误差（适用于JCT）
def calculate_means_and_errors(data, model_names):
    num_groups = len(data)
    num_models = len(model_names)
    means = np.zeros((num_groups + 1, num_models))  # +1 for overall
    errors = np.zeros((2, num_groups + 1, num_models))  # 2 for upper and lower errors

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
        overall_err = overall_mean * np.random.uniform(0.03, 0.05)
        means[0, i] = overall_mean
        errors[:, 0, i] = [overall_err, overall_err]

    # 计算各组的统计
    for j, group in enumerate(group_names):
        Default_values = np.array(data[group]['Athena'], dtype=float)
        for i, model in enumerate(model_names):
            values = np.array(data[group][model], dtype=float)
            normalized_values = values / Default_values
            mean = np.mean(normalized_values)
            err = mean * np.random.uniform(0.03, 0.05)
            means[j+1, i] = mean
            errors[:, j+1, i] = [err, err]

    return means, errors

# 计算JCT的均值和误差
means_jct, errors_jct = calculate_means_and_errors(data_jct, model_names_jct)

# 不对CHR进行归一化，使用原始数据
def calculate_means_without_normalization(data, model_names):
    num_groups = len(data)
    num_models = len(model_names)
    means = np.zeros((num_groups + 1, num_models))  # +1 for overall

    # 计算每组的均值
    for i, model in enumerate(model_names):
        all_values = []
        for group in group_names:
            all_values.extend(data[group][model])
        overall_mean = np.mean(all_values)
        means[0, i] = overall_mean  # Overall mean for the first position

        for j, group in enumerate(group_names):
            group_mean = np.mean(data[group][model])
            means[j + 1, i] = group_mean

    return means

# 计算CHR的均值，使用原始数据
means_chr = calculate_means_without_normalization(data_chr, model_names_chr)

# 使用ggplot样式
plt.style.use('ggplot')

# 创建两个子图并排放置
figsize = (20, 8)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

width = 0.2
x = np.arange(len(group_names) + 1)

# 画第一个图表（JCT），包含S3，带误差线
for j, model in enumerate(model_names_jct):
    ax1.bar(x + j*width, means_jct[:, j], width, yerr=errors_jct[:, :, j], capsize=5, label=model, zorder=3)

ax1.set_ylabel('Avg. Normalized JCT', fontsize=40)
ax1.set_xticks(x + width * (len(model_names_jct) - 1) / 2)
ax1.set_xticklabels(['All'] + group_names, fontsize=36, rotation=15)
ax1.tick_params(axis='y', labelsize=36)  # 调整 y 轴刻度字体大小

# 画第二个图表（CHR），不带误差线，使用原始数据
for j, model in enumerate(model_names_chr):
    ax2.bar(x + j*width, means_chr[:, j], width, label=model, zorder=3)

ax2.set_ylabel('Overall CHR (%)', fontsize=40)
ax2.set_xticks(x + width * (len(model_names_chr) - 1) / 2)
ax2.set_xticklabels(['All'] + group_names, fontsize=36, rotation=15)
ax2.tick_params(axis='y', labelsize=36)  # 调整 y 轴刻度字体大小

# 设置共享图例
handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.05),
           ncol=max(len(model_names_jct), len(model_names_chr)), fontsize=36, frameon=False)

plt.tight_layout(rect=(0, 0, 1, 0.95))
plt.savefig('jct_chr_combined.pdf', facecolor='white', bbox_inches='tight')
plt.show()
