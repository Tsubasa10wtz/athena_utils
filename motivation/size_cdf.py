import boto3
import matplotlib.pyplot as plt
import numpy as np

def get_s3_file_sizes(bucket_name, aws_access_key_id, aws_secret_access_key, prefix):
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)
    paginator = s3.get_paginator('list_objects_v2')
    operation_parameters = {'Bucket': bucket_name, 'Prefix': prefix}

    file_sizes = []

    for page in paginator.paginate(**operation_parameters):
        if 'Contents' in page:
            for obj in page['Contents']:
                file_sizes.append(obj['Size'] / (1024 * 1024))  # 转换为MB

    return file_sizes

bucket_name = 'alluxiobucket'
aws_access_key_id = 'AKIAUTMJIZIJE5HMS7HY'
aws_secret_access_key = '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'

prefix = 'alluxio/Datasets/ImageNet/test/'  # 替换为你的S3路径前缀

file_sizes = get_s3_file_sizes(bucket_name, aws_access_key_id, aws_secret_access_key, prefix)

# 将数据排序以确保CDF正确
file_sizes = sorted(file_sizes)

# 计算CDF
cdf = np.cumsum(np.ones_like(file_sizes)) / len(file_sizes)

plt.rcParams.update({'font.size': 24})  # 设置字体大小

# 绘制CDF图
plt.figure(figsize=(10, 6))
plt.plot(file_sizes, cdf, marker='.', linestyle='none', color='blue')

# 在横轴为4处绘制一条垂直分界线
plt.axvline(x=4, color='red', linestyle='--', linewidth=2)

# 添加标注
plt.text(4.1, 0.5, '4 MB', color='red', fontsize=14, verticalalignment='center')

plt.xlabel('File Size (MB)')
plt.ylabel('CDF')
plt.grid(True)

# 保存为PDF
plt.savefig('cdf.pdf', facecolor='white', bbox_inches='tight')
