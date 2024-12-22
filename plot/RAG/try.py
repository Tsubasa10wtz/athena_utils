# 统计txt文件的行数
def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到!")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

# 使用示例
file_path = 'filtered_triviaqa_diskann.txt'  # 替换为你的文件路径
line_count = count_lines(file_path)

if line_count is not None:
    print(f"文件 '{file_path}' 的行数是: {line_count}")