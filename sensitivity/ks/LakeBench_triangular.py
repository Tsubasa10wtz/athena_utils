import ast
import pandas as pd
from scipy.stats import kstest
from sensitivity.ks.ks_test import calculate_diff_mean_and_variance, triangular_cdf
import seaborn as sns
import matplotlib.pyplot as plt

def generate_file_number_map(filename_list_path):
    with open(filename_list_path, "r", encoding="utf-8") as file:
        files = [line.strip() for line in file]
    files.sort()
    file_number_map = {file_name: idx for idx, file_name in enumerate(files, start=1)}
    return file_number_map

def extract_column_from_csv_with_pandas(csv_file, query_col, candidate_col):
    df = pd.read_csv(csv_file)
    merged_list = []
    for _, row in df.iterrows():
        query_table_item = row[query_col]
        candidate_table_items = ast.literal_eval(row[candidate_col])
        merged_list.append(query_table_item)
        merged_list.extend(candidate_table_items)
    return merged_list

def map_column_data_to_numbers(column_data, file_number_map):
    none_items = []
    mapped_data = []
    for idx, item in enumerate(column_data):
        mapped_value = file_number_map.get(item, None)
        if mapped_value is None:
            none_items.append((idx, item))
        mapped_data.append(mapped_value)
    if none_items:
        print("Mapped to None:")
        for index, item in none_items:
            print(f"Index: {index}, Item: {item}")
    return mapped_data

def calculate_absolute_differences(mapped_data):
    differences = [abs(mapped_data[i] - mapped_data[i - 1]) for i in range(1, len(mapped_data))]
    return differences

# 设置目标目录路径
filename_list_path = "/Users/wangtianze/直博/项目/Athena/athena/lakebench/join/filename_list.txt"

# 生成文件路径到编号的映射
file_number_map = generate_file_number_map(filename_list_path)

# 示例 CSV 文件路径
csv_file_path = '/Users/wangtianze/直博/项目/Athena/athena/lakebench/join/opendata_join_result_grouped.csv'

# 提取指定列的数据
data = extract_column_from_csv_with_pandas(csv_file_path, 'query_table', 'candidate_table')

# 按编号映射列数据
mapped_data = map_column_data_to_numbers(data, file_number_map)

ids = mapped_data


# 设置 c 参数
c = 2829

# 统计 p 值分布
p_values = []
batch_size = 100

# 按批次处理数据
for i in range(0, len(ids), batch_size):
    # 提取一个批次的数据
    batch = ids[i:i + batch_size]
    if len(batch) < batch_size:
        break  # 忽略不足一个批次的数据

    # 计算当前批次的差值
    diff = calculate_diff_mean_and_variance(batch)

    # 执行 K-S 检验
    result = kstest(diff, triangular_cdf, args=(c,))
    p_values.append(result.pvalue)

# 统计 p 值 >= 0.01 的数量
count_ge_0_01 = sum(1 for p in p_values if p >= 0.01)

# 统计 p 值 < 0.01 的数量
count_lt_0_01 = sum(1 for p in p_values if p < 0.01)

# 统计 p 值 >= 0.05 的数量
count_ge_0_05 = sum(1 for p in p_values if p >= 0.05)

# 统计 p 值 < 0.05 的数量
count_lt_0_05 = sum(1 for p in p_values if p < 0.05)



# 输出结果
print(f"Number of p-values >= 0.01: {count_ge_0_01}")
print(f"Number of p-values < 0.01: {count_lt_0_01}")
print(f"Number of p-values >= 0.05: {count_ge_0_05}")
print(f"Number of p-values < 0.05: {count_lt_0_05}")
print(f"P-values: {p_values}")