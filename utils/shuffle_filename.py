import os
import random

# 指定目标目录
directory = "/mnt/jfs"  # 替换为你的目标目录路径

# 获取目录下所有文件名
file_names = os.listdir(directory)

# 随机打乱文件名
random.shuffle(file_names)

# 打印前100个文件名
for file_name in file_names[:100]:
    print(file_name)