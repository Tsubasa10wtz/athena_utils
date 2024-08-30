import boto3
import matplotlib.pyplot as plt


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
                file_sizes.append(obj['Size'])

    return file_sizes

bucket_name = 'alluxiobucket'
aws_access_key_id = 'AKIAUTMJIZIJE5HMS7HY'
aws_secret_access_key = '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'

prefix = 'alluxio/Datasets/ImageNet/test/'  # 替换为你的S3路径前缀

file_sizes = get_s3_file_sizes(bucket_name, aws_access_key_id, aws_secret_access_key, prefix)

# 绘制箱线图
plt.figure(figsize=(10, 6))
plt.boxplot(file_sizes, vert=False)
plt.xlabel('File Size (Bytes)')
plt.title('Distribution of S3 File Sizes')
plt.show()