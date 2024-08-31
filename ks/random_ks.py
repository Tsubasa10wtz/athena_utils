import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kstest

# 定义cluster_info
cluster_info = {
    10: 500894,
    25: 15369,
    31: 65389,
    32: 40366,
    35: 61748,
    38: 70260,
    39: 74164,
}

# 存储所有cluster的p值
all_p_values = []
min_p_values={}


def triangular_cdf(x, c):
    """三角分布的CDF函数"""
    return np.where(x < 0, 0, np.where(x > c, 1, ((2 * x * c - x ** 2) / c ** 2)))


# 计算每个cluster的p值
for cluster_num, c in cluster_info.items():
    # 生成随机ID数据

    ids = np.arange(c)
    np.random.shuffle(ids)

    # 计算相邻ID的差值
    diffs = np.abs(np.diff(ids))

    # 计算p值
    p_values = []
    step_size = 50
    for i in range(0, len(diffs), step_size):
        diff_list = diffs[i:i + step_size]
        if len(diff_list) < step_size:
            break
        result = kstest(diff_list, triangular_cdf, args=(c,))
        p_values.append(result.pvalue)

    # 将p值添加到总列表中
    all_p_values.append(p_values)
    min_p_values[cluster_num] = min(p_values) if p_values else None

# 绘制所有cluster的箱线图
plt.style.use("fivethirtyeight")
plt.rcParams.update({'font.size': 14})  # 设置字体大小

fig, ax = plt.subplots(figsize=(10, 8))

plt.boxplot(all_p_values, medianprops={'color': 'black', 'linewidth': '1.5'},
            patch_artist=True,
            boxprops={'facecolor': '#add8e6'},
            widths=0.2,
            meanline=False,
            showmeans=False,
            flierprops={"marker": "o", "markerfacecolor": "#ffa500", "markersize": 10},
            labels=[f'Random {n}' for n in range(1,8)])

# 添加一条表示 p-value = 0.05 的水平线
ax.axhline(y=0.000001, color='red', linestyle='--', linewidth=2)
ax.text(0.05, 0.08, 'y=1e-6', color='red', fontsize=20, transform=ax.transAxes)  # 添加文本标注

plt.yscale('log')
plt.ylabel('p-value (log scale)')
plt.tight_layout()
plt.show()

for cluster_num, min_p_value in min_p_values.items():
    print(f"Cluster {cluster_num} 最小 p-value: {min_p_value}")
