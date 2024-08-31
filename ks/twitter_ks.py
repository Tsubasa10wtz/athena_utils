import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import kstest

# 定义文件路径的模板
file_path_template = '../trace/twitter/cache-trace/samples/2020Mar/cluster{:03d}'

# 初始化存储结果的列表
all_p_values = []


# 假设你要处理的cluster编号及对应的c值
cluster_info = {
    #cluster_id:files
    # 7: 201863,
    # 9: 72147,
    # 14: 91055,
    # 19: 633350,
    # 20: 111986,
    10: 500894,
    25: 15369,
    # 27: 622347,
    31: 65389,
    32: 40366,
    35: 61748,
    38: 70260,
    39: 74164,

}

max_p_values = {}

for cluster_num, c in cluster_info.items():
    file_path = file_path_template.format(cluster_num)

    # 读取CSV文件，跳过格式错误的行
    data = pd.read_csv(file_path, header=None, on_bad_lines='skip')

    # 将所有列转换为字符串类型
    data = data.astype(str)

    # 筛选包含“get”字段的行（注意是第七列，索引为6）
    data = data[data[5].str.contains('get', case=False, na=False)]

    # 对第二列进行字典序编号
    data['sorted_index'] = data[1].rank(method='dense').astype(int)

    # 计算相邻行编号的差值
    data['diff'] = data['sorted_index'].diff().dropna().astype(int).abs()


    def triangular_cdf(x, c):
        return np.where(x < 0, 0, np.where(x > c, 1, ((2 * x * c - x ** 2) / c ** 2)))


    # 初始化 p-value 列表
    p_values = []

    # 每隔 50 项计算一次 p-value
    step_size = 50
    for i in range(1, 2001, step_size):
        diff_list = data['diff'].tolist()[i:i + step_size]
        if len(diff_list) < step_size:
            break
        result = kstest(diff_list, triangular_cdf, args=(c,))
        p_values.append(result.pvalue)

    # 将该cluster的p-values添加到总列表中
    all_p_values.append(p_values)
    max_p_values[cluster_num] = max(p_values) if p_values else None

# 绘制所有cluster的箱线图
plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 14})  # 设置字体大小

fig, ax = plt.subplots(figsize=(10, 8))

plt.boxplot(all_p_values, medianprops={'color': 'black', 'linewidth': '1.5'},
            patch_artist=True,
            boxprops={'facecolor':'#ffa500'},
            widths=0.21,
            meanline=False,
            showmeans=False,
            flierprops={"marker": "o", "markerfacecolor": "#add8e6", "markersize": 10},
            labels=[f'Cluster {n}' for n in cluster_info.keys()])

# 添加一条表示 p-value = 0.05 的水平线
ax.axhline(y=0.05, color='red', linestyle='--', linewidth=2)
ax.text(0.5, 0.5, 'p=0.05', color='red', fontsize=14)  # 添加文本标注

plt.yscale('log')
plt.ylabel('p-value (log scale)')
plt.tight_layout()
plt.show()

# 输出每个 cluster 的最大 p-value
for cluster_num, max_p_value in max_p_values.items():
    print(f"Cluster {cluster_num} 最大 p-value: {max_p_value}")
