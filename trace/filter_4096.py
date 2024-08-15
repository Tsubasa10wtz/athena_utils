import pandas as pd

# 读取CSV文件
file_path = 'filtered_data.csv'  # 将此路径替换为实际文件路径
data = pd.read_csv(file_path, header=None)

# 标记连续的第六列为4096的行
data['is_4096'] = data[5] == 4096

# 计算连续的最大长度及其起始和结束索引
max_len = 0
current_len = 0
start_index = 0
current_start = 0

for i in range(len(data)):
    if data['is_4096'].iloc[i]:
        if current_len == 0:
            current_start = i
        current_len += 1
        if current_len > max_len:
            max_len = current_len
            start_index = current_start
    else:
        current_len = 0

end_index = start_index + max_len

# 提取最长的连续4096的行
longest_4096_sequence = data.iloc[start_index:end_index]

# 删除临时列
longest_4096_sequence = longest_4096_sequence.drop(columns=['is_4096'])

# 输出结果
output_file_path = 'longest_4096_sequence.csv'  # 将此路径替换为输出文件路径
longest_4096_sequence.to_csv(output_file_path, header=False, index=False)

print(f"Longest sequence of rows with the sixth column as 4096 saved to {output_file_path}")
