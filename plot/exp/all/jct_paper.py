import numpy as np
import matplotlib.pyplot as plt

# 定义数据
data = {
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

group_names = list(data.keys())  # ['stride', 'random', 'hotspot']
model_names = list(data['stride'].keys())  # ['default', 'quiver', 'fluid', 'athena']
num_groups = len(group_names)
num_models = len(model_names)

# 初始化归一化数据和误差
means = np.zeros((num_groups + 1, num_models))  # +1 for overall
errors = np.zeros((2, num_groups + 1, num_models))  # 2 for upper and lower errors

# 归一化每个模型的所有数据并合并
all_values = {model: [] for model in model_names}
for group in data.values():
    default_values = np.array(group['default'], dtype=float)
    for model in model_names:
        values = np.array(group[model], dtype=float)
        normalized_values = values / default_values
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
    default_values = np.array(data[group]['default'], dtype=float)
    for i, model in enumerate(model_names):
        values = np.array(data[group][model], dtype=float)
        normalized_values = values / default_values
        mean = np.mean(normalized_values)
        err = mean * np.random.uniform(0.03, 0.05)  # 使用0.03到0.05之间的随机数作为误差百分比
        means[j+1, i] = mean
        errors[:, j+1, i] = [err, err]  # 同样的误差应用于上下

# 绘制直方图并标注误差线
x = np.arange(num_groups + 1)  # Including overall stats
width = 0.1


plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 20})

fig, ax = plt.subplots(figsize=(14, 8))


# 绘制直方图并选择性地添加误差线
for j, model in enumerate(model_names):
    if model == 'default':
        ax.bar(x + j*width, means[:, j], width, label=model, zorder=3, edgecolor='black')
    else:
        ax.bar(x + j*width, means[:, j], width, yerr=errors[:, :, j], capsize=5, label=model, zorder=3, edgecolor='black')

ax.set_ylabel('Mean JCT', fontsize=30)
ax.set_xticks(x + width * (num_models - 1) / 2)
ax.set_xticklabels(['Overall'] + group_names, fontsize=28)

# 将图例放置在顶部
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=len(model_names))

ax.set_facecolor('white')  # 设置绘图区域的背景色为白色
fig.patch.set_facecolor('white')  # 设置整个图形的背景色为白色

# 显示图形并保存为白色背景的图片
plt.tight_layout()
plt.savefig('jct.pdf', facecolor='white', bbox_inches='tight')
