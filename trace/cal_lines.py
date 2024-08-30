def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# 示例用法
file_path = 'twitter/cache-trace/samples/2020Mar/cluster054'
line_count = count_lines_in_file(file_path)
print(f"Total number of lines: {line_count}")
