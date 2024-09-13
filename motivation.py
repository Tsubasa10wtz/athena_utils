import os

def count_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        count += len(files)
    return count

directory_path = '/var/jfsCache/3ecabab3-a684-4d83-868c-11cdc2b54ca0/raw/chunks'
file_count = count_files(directory_path)
print("文件数量：", file_count)