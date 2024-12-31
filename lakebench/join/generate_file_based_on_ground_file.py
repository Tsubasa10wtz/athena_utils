import csv
import os
import shutil
import pandas as pd


def extract_column_from_csv_with_pandas(csv_file, query_col, candidate_col):
    # 使用 pandas 读取 CSV 文件
    df = pd.read_csv(csv_file)

    # 初始化合并后的列表
    merged_list = []

    # 遍历每一行
    for _, row in df.iterrows():
        # 获取 query_table 数据
        query_table_item = row[query_col]

        # 获取 candidate_table 数据
        candidate_table_item = row[candidate_col]

        # 将 query_table_item 和 candidate_table_item 合并
        merged_list.append(query_table_item)  # 先添加 query_table_item
        merged_list.append(candidate_table_item)  # 然后添加 candidate_table_item

    return merged_list



def generate_csv_files_from_sample(sample_file_path, directory_path, unique_data):
    # 确保目录存在
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # 复制 sample.csv 文件并命名为 unique_data 中的每个值
    for item in unique_data:
        # 定义目标文件路径
        new_file_path = os.path.join(directory_path, item)

        # 复制文件并重命名
        shutil.copy(sample_file_path, new_file_path)

        print(f"File {new_file_path} created successfully.")



# 设置目标目录路径
directory_path = "data"

# 从opendata_join_ground_truth.csv就可以得到所有文件（后续通过list(set(data))过滤），为了和find_ground_truth.py生成文件的功能分开
csv_file_path = '/Users/wangtianze/Downloads/opendata_join_ground_truth.csv'

with open(csv_file_path, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)

print(f"The number of rows in the CSV file is: {row_count}")

# 提取指定列的数据
data = extract_column_from_csv_with_pandas(csv_file_path, 'query_table', 'candidate_table')

print(f"data length: {len(data)}")

# 创建一个目标大小的 sample.csv 文件
sample_file_path = "sample.csv"

# 获取唯一的数据
unique_data = list(set(data))
print(f"unique length: {len(unique_data)}")

# 基于 sample.csv 生成多个目标文件
generate_csv_files_from_sample(sample_file_path, directory_path, unique_data)