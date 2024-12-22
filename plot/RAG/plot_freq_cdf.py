import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 从 CSV 文件读取数据
file_path = "doc_frequency_test_hnsw_filename.csv"  # 替换为您的文件路径
data = pd.read_csv(file_path)

# 确保数据有 "Frequency" 列
if "Frequency" not in data.columns:
    raise ValueError("The CSV file must contain a 'Frequency' column.")

# 按 Frequency 升序排序
data_sorted = data.sort_values(by="Frequency")

# 计算累积频率和 CDF
data_sorted['Cumulative Frequency'] = data_sorted['Frequency'].cumsum()
total_frequency = data_sorted['Frequency'].sum()
data_sorted['CDF'] = data_sorted['Cumulative Frequency'] / total_frequency

# 计算文档比率
data_sorted['Ratio of Docs'] = np.arange(1, len(data_sorted) + 1) / len(data_sorted)

# 绘制 CDF 图
plt.figure(figsize=(8, 6))
plt.plot(data_sorted['Ratio of Docs'], data_sorted['CDF'], marker='o', linestyle='-')
plt.xscale('log')
plt.yscale('linear')
plt.xticks([10**-5, 10**-4, 10**-3, 10**-2, 10**-1], labels=['$10^{-5}$', '$10^{-4}$', '$10^{-3}$', '$10^{-2}$', '$10^{-1}$'])
plt.xlabel("Ratio of Docs (log scale)")
plt.ylabel("Cumulative Frequency")
plt.title("CDF of Document Frequency")
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.show()