def extract_parquet_lines(log_file_path, output_file_path):
    try:
        # 打开日志文件读取数据
        with open(log_file_path, 'r') as log_file:
            # 打开输出文件准备写入
            with open(output_file_path, 'w') as output_file:
                # 逐行读取日志文件
                for line in log_file:
                    # 检查行中是否包含关键字 "parquet"
                    if 'parquet' in line:
                        # 写入找到的行到输出文件
                        output_file.write(line)
        print("文件处理完成，包含 'parquet' 的行已保存至", output_file_path)
    except FileNotFoundError:
        print("指定的文件未找到，请检查文件路径是否正确。")
    except Exception as e:
        print("处理文件时出错:", e)

# 使用示例
log_file_path = 'spark-10.log'  # 日志文件路径
output_file_path = 'output_file.txt'  # 输出文件路径
extract_parquet_lines(log_file_path, output_file_path)