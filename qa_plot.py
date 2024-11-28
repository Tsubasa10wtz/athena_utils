import json
from collections import Counter
import matplotlib.pyplot as plt

# JSON文件路径
file_path = "/Users/wangtianze/Downloads/web-test-without-answers.json"

# 读取JSON文件
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# 提取Filename字段
def extract_filenames(data):
    filenames = []
    if "Data" in data:
        for item in data["Data"]:
            # 从EntityPages提取Filename
            if "EntityPages" in item:
                for entity in item["EntityPages"]:
                    if "Filename" in entity:
                        filenames.append(entity["Filename"])
            # 从SearchResults提取Filename
            if "SearchResults" in item:
                for result in item["SearchResults"]:
                    if "Filename" in result:
                        filenames.append(result["Filename"])
    return filenames

# 统计Filename出现次数
def count_filenames(data):
    filenames = extract_filenames(data)
    return Counter(filenames)

# 调用函数统计
filename_counts = count_filenames(data)

# 按出现次数从多到少排序
sorted_filename_counts = sorted(filename_counts.items(), key=lambda x: x[1], reverse=True)

# 计算前20%和后80%的出现次数总和
num_files_20_percent = int(len(sorted_filename_counts) * 0.2)
top_20_percent_sum = sum(count for filename, count in sorted_filename_counts[:num_files_20_percent])
bottom_80_percent_sum = sum(count for filename, count in sorted_filename_counts[num_files_20_percent:])

# 准备数据绘图
categories = ['Top 20%', 'Bottom 80%']
counts = [top_20_percent_sum, bottom_80_percent_sum]

# 绘制柱状图
plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color=['blue', 'green'])
plt.xlabel('Category', fontsize=20)
plt.ylabel('Count of Occurrences', fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Comparison of Filename Occurrences', fontsize=24)
plt.savefig('distribution.pdf', facecolor='white', bbox_inches='tight')
