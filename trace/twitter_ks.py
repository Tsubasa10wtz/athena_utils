import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from scipy.stats import kstest

# 定义文件路径的模板
file_path_template = 'twitter/cache-trace/samples/2020Mar/cluster{:03d}'

# 初始化存储结果的列表
mean_diffs = []
variance_diffs = []
total_counts = []
all_mappings = {}  # 用于存储每个cluster的编号映射

plt.style.use("ggplot")
plt.rcParams.update({'font.size': 24})


file_path = file_path_template.format(35)


# 读取CSV文件，跳过格式错误的行
data = pd.read_csv(file_path, header=None, on_bad_lines='skip')

# 将所有列转换为字符串类型
data = data.astype(str)

# 筛选包含“get”字段的行（注意是第七列，索引为6）
data = data[data[5].str.contains('get', case=False, na=False)]


# 对第二列进行字典序编号
data['sorted_index'] = data[1].rank(method='dense').astype(int)

# 记录每个cluster的第一列和编号的对应关系
id_to_index_mapping = {row[1]: row['sorted_index'] for idx, row in data.iterrows()}
all_mappings[f"cluster{35:03d}"] = id_to_index_mapping

# 计算相邻行编号的差值
data['diff'] = data['sorted_index'].diff().dropna().astype(int).abs()

def triangular_cdf(x, c):
    return np.where(x < 0, 0, np.where(x > c, 1, ((2*x*c-x**2)/c**2)))

# 假设 c 已知
c = 61748

diff_list = data['diff'].tolist()[1:301]
print(diff_list)



# 执行KS检验
result = kstest(diff_list, triangular_cdf, args=(c,))
print('KS statistic:', result.statistic)
print('p-value:', result.pvalue)


print("Total number of unique indices:", data['sorted_index'].nunique())