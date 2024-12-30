import os


def calculate_average_file_size(directory_path):
    # 获取目录下所有文件（不包括子目录）
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # 如果目录为空或没有文件，返回 None
    if not files:
        return None

    total_size = 0

    # 计算所有文件的总大小
    for file in files:
        file_path = os.path.join(directory_path, file)
        total_size += os.path.getsize(file_path)

    # 计算平均大小
    average_size = total_size / len(files)

    print(len(files))
    print(f"文件总大小为: {total_size / 1024 / 1024:.2f} MB")

    return average_size


# 示例目录路径
directory_path = "/Users/wangtianze/Downloads/opendata_union_query"

# 计算并打印平均文件大小
average_size = calculate_average_file_size(directory_path)
if average_size is not None:
    print(f"平均文件大小为: {average_size / 1024 / 1024:.2f} MB")
else:
    print("该目录没有文件或目录为空。")

