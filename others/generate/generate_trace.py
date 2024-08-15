import os
import csv


# 输入和输出文件路径
path = '../tracec_run_basic_hotspot.txt'
output_csv_path = '../ycsb-1g_trace_hotspot.csv'

with open(path, 'r') as file, open(output_csv_path, 'w', newline='') as csv_file:
    # 创建CSV writer对象
    csv_writer = csv.writer(csv_file)
    # 逐行读取文件内容
    for line in file:
        parts = line.split(' ')
        if parts[0] == 'READ':
            file_name = f'{parts[2]}.txt'
            # 写入file_name到CSV文件
            csv_writer.writerow([file_name])

print(f"CSV file has been written to {output_csv_path}")