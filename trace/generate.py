import os
import pandas as pd

# 加载CSV文件
df = pd.read_csv('twitter/cache-trace/samples/2020Mar/cluster035', header=None)  # 假设CSV文件没有列标题

# 筛选包含“get”字段的行（注意是第六列，索引为5）
df = df[df[5].str.contains('get', case=False, na=False)]

# 计算每项的大小为第三列和第四列的和，并将其添加为新列
df['size'] = df[2] + df[3]

# 创建一个新的文件夹 'cluster035'
output_dir = 'cluster035'
os.makedirs(output_dir, exist_ok=True)

# 筛选出第二列中的所有不同项
unique_items = df.drop_duplicates(subset=[1])

# 为每个不同项创建一个对应的txt文件
for _, row in unique_items.iterrows():
    file_name = os.path.join(output_dir, f"{row[1]}.txt")

    # 根据大小创建文件
    with open(file_name, 'wb') as f:
        f.write(b'\0' * 15 * 1024)

print(f"已生成 {len(unique_items)} 个文件，每个文件对应第二列中的不同项，并存储在 '{output_dir}' 文件夹中。")
