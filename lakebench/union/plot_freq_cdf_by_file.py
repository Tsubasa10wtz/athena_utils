import ast
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

def generate_file_number_map(filename_list_path):
    # 获取目录中的所有文件（不包括子目录）并排除 .DS_Store
    with open(filename_list_path, "r", encoding="utf-8") as file:
        # 逐行读取文件内容并去掉换行符
        files = [line.strip() for line in file]

    # 对文件名进行字典序排序
    files.sort()

    # 创建一个字典来保存文件路径到编号的映射
    file_number_map = {}

    # 遍历排序后的文件列表并为每个文件分配编号
    for idx, file_name in enumerate(files, start=1):

        # 将文件路径映射到编号
        file_number_map[file_name] = idx

    return file_number_map


def extract_column_from_csv_with_pandas(csv_file, query_col, candidate_col):
    # 使用 pandas 读取 CSV 文件
    df = pd.read_csv(csv_file)

    # 初始化合并后的列表
    merged_list = []

    # 遍历每一行
    for _, row in df.iterrows():
        # 获取 query_table 数据
        query_table_item = row[query_col]

        # 将 candidate_table 列中的字符串转换为列表
        candidate_table_items = ast.literal_eval(row[candidate_col])

        # 将 query_table 和 candidate_table 列表中的所有项合并
        merged_list.append(query_table_item)  # 先添加 query_table_item
        merged_list.extend(candidate_table_items)  # 然后添加所有 candidate_table_items

    return merged_list


def map_column_data_to_numbers(column_data, file_number_map):
    # 记录被映射为 None 的项及其索引
    none_items = []

    # 将列数据映射为编号
    mapped_data = []
    for idx, item in enumerate(column_data):
        mapped_value = file_number_map.get(item, None)
        if mapped_value is None:
            none_items.append((idx, item))  # 记录索引和原始值
        mapped_data.append(mapped_value)

    # 打印出所有被映射为 None 的项
    if none_items:
        print("Mapped to None:")
        for index, item in none_items:
            print(f"Index: {index}, Item: {item}")

    return mapped_data


def calculate_absolute_differences(mapped_data):
    # 计算相邻项之间的绝对差值
    differences = [abs(mapped_data[i] - mapped_data[i - 1]) for i in range(1, len(mapped_data))]
    return differences


def count_and_fill_missing_files(directory_path, item_counts):
    # 获取目录中的所有文件（不包括子目录）并排除 .DS_Store
    with open(filename_list_path, "r", encoding="utf-8") as file:
        # 逐行读取文件内容并去掉换行符
        files = [line.strip() for line in file]

    # 将文件列表转换为 pandas 的 Series，并用 0 填补缺失的项
    file_series = pd.Series(files)

    # 使用 reindex() 方法，将文件列表与 item_counts 对齐，缺失的项填为 0
    filled_counts = item_counts.reindex(file_series, fill_value=0)

    # 按照出现次数从大到小排序
    sorted_filled_counts = filled_counts.sort_values(ascending=False)

    return sorted_filled_counts


def plot_cdf(sorted_filled_counts):
    # 计算累计出现次数
    cumulative_counts = sorted_filled_counts.cumsum()

    # 计算总的出现次数
    total_counts = cumulative_counts.iloc[-1]

    # 计算累计出现次数占总数的比例
    cdf_values = cumulative_counts / total_counts

    # 计算文件比率
    file_count = len(sorted_filled_counts)
    file_ratios = (pd.Series(range(1, file_count + 1))) / file_count  # 使用整数序列

    # 绘制 CDF 图
    # plt.style.use("fivethirtyeight")
    plt.rcParams['font.family'] = 'Arial Unicode MS'  # 确保支持中文字体
    plt.figure(figsize=(14, 6))
    plt.plot(file_ratios, cdf_values, marker='.', linestyle='-', color='b')
    plt.xlabel('Ratio of Item', fontsize=44)
    plt.ylabel('CDF', fontsize=44)
    plt.grid(True)

    # 设置 x 轴和 y 轴的刻度字体大小
    plt.tick_params(axis='x', labelsize=24)  # x 轴刻度字体大小
    plt.tick_params(axis='y', labelsize=24)  # y 轴刻度字体大小

    # 调整坐标轴刻度
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x * 100:.0f}%'))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(0.1))

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x * 100:.0f}%'))
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.2))

    # 显示图表
    plt.tight_layout()

    plt.savefig('skewed_cdf.pdf', facecolor='white', bbox_inches='tight')

    plt.show()

# 设置目标目录路径
filename_list_path = "/Users/wangtianze/直博/项目/Athena/athena/lakebench/union/filename_list.txt"

# 生成文件路径到编号的映射
file_number_map = generate_file_number_map(filename_list_path)

# 示例 CSV 文件路径
csv_file_path = '/Users/wangtianze/直博/项目/Athena/athena/lakebench/union/opendata_union_result_grouped.csv'

# 提取指定列的数据
data = extract_column_from_csv_with_pandas(csv_file_path, 'query_table', 'candidate_table')

# 使用 pandas 统计每个项的出现次数
item_counts = pd.Series(data).value_counts()

# 对缺失的文件进行填充，未出现的文件计数为 0
sorted_filled_counts = count_and_fill_missing_files(filename_list_path, item_counts)

# 绘制 CDF
plot_cdf(sorted_filled_counts)

