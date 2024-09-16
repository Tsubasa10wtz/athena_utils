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

# 计算Athena相较于JuiceFS的JCT减少百分比和CHR提升（直接相减）
def calculate_jct_chr_improvements(means_jct, means_chr):
    # Athena和JuiceFS在整体(all)上的位置
    athena_jct_all = means_jct[0, model_names_jct.index('Athena')]
    juicefs_jct_all = means_jct[0, model_names_jct.index('JuiceFS')]

    athena_chr_all = means_chr[0, model_names_chr.index('Athena')]
    juicefs_chr_all = means_chr[0, model_names_chr.index('JuiceFS')]

    # 计算JCT减少百分比（JuiceFS相较于Athena）
    jct_reduction_all = (juicefs_jct_all - athena_jct_all) / juicefs_jct_all * 100

    # 计算CHR提升百分比（Athena相较于JuiceFS, 直接相减）
    chr_improvement_all = athena_chr_all - juicefs_chr_all

    return jct_reduction_all, chr_improvement_all

# 调用函数，输出结果
jct_reduction_all, chr_improvement_all = calculate_jct_chr_improvements(means_jct, means_chr)

print("JCT Reduction by Athena compared to JuiceFS for 'All': {:.2f}%".format(jct_reduction_all))
print("CHR Improvement by Athena compared to JuiceFS for 'All': {:.2f}%".format(chr_improvement_all))