import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 定义总文档数量
total_documents = 73942  # 假设总文档数为 1000

# 从 CSV 文件读取数据
file_path = "doc_frequency_train_diskann_filename.csv"  # 替换为您的文件路径
data = pd.read_csv(file_path)

# 确保数据有 "Frequency" 列
if "Frequency" not in data.columns:
    raise ValueError("The CSV file must contain a 'Frequency' column.")

# 补全缺失的文档频率为 0
# 当前已有文档数量
current_documents = len(data)
missing_documents = total_documents - current_documents

# 如果有缺失的文档
if missing_documents > 0:
    # 创建一个 DataFrame 表示缺失的文档，频率为 0
    missing_data = pd.DataFrame({
        "Document ID": [f"Missing_Doc_{i}" for i in range(1, missing_documents + 1)],
        "Frequency": [0] * missing_documents
    })
    # 合并到原数据
    data = pd.concat([data, missing_data], ignore_index=True)

# 按 Frequency 升序排序
# data_sorted = data.sort_values(by="Frequency")
# 按 Frequency 降序排序
data_sorted = data.sort_values(by="Frequency", ascending=False)

# 计算累积频率和 CDF
data_sorted['Cumulative Frequency'] = data_sorted['Frequency'].cumsum()
total_frequency = data_sorted['Frequency'].sum()
data_sorted['CDF'] = data_sorted['Cumulative Frequency'] / total_frequency

# 计算文档比率
data_sorted['Ratio of Docs'] = np.arange(1, len(data_sorted) + 1) / len(data_sorted)

# 绘制 CDF 图
plt.figure(figsize=(16, 6))
plt.plot(data_sorted['Ratio of Docs'], data_sorted['CDF'], marker='o', linestyle='-')
plt.xscale('log')
plt.yscale('linear')
plt.xticks([10**-5, 10**-4, 10**-3, 10**-2, 10**-1], labels=['$10^{-5}$', '$10^{-4}$', '$10^{-3}$', '$10^{-2}$', '$10^{-1}$'], fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel("Ratio of Docs (log scale)", fontsize=40)
plt.ylabel("CDF",fontsize=40)
plt.title("CDF of Document Frequency")
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()