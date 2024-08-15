import pandas as pd

# 读取CSV文件
file_path = 'MSR-Cambridge/proj_3.csv'  # 将此路径替换为实际文件路径
data = pd.read_csv(file_path, header=None)

# 筛选出第四列值为"Read"的行
filtered_data = data[data[3] == 'Read']

# 保存到新的CSV文件，不包含header
output_file_path = 'filtered_data.csv'  # 将此路径替换为输出文件路径
filtered_data.to_csv(output_file_path, header=False, index=False)

print(f"Filtered data saved to {output_file_path}")
