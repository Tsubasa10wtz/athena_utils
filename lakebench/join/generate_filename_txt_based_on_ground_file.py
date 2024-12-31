# 仅仅生成一个含有全部文件名的txt文件
import csv
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


# 示例 CSV 文件路径
csv_file_path = '/Users/wangtianze/Downloads/opendata_join_ground_truth.csv'

# 统计行数
with open(csv_file_path, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)

print(f"The number of rows in the CSV file is: {row_count}")

# 提取指定列的数据
data = extract_column_from_csv_with_pandas(csv_file_path, 'query_table', 'candidate_table')

print(f"data length: {len(data)}")

# 获取唯一数据
unique_data = list(set(data))
print(f"unique length: {len(unique_data)}")

# 写入 TXT 文件
output_txt_file_name = "filename_list.txt"

with open(output_txt_file_name, "w", encoding="utf-8") as file:
    for item in unique_data:
        file.write(f"{item}\n")

print(f"Unique data has been written to {output_txt_file_name}")
