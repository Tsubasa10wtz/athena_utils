def count_unique_lines(filename):
    unique_numbers = set()  # 用于存储唯一的数字
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # 确保不处理空行
                number = line.split(':')[0]  # 获取冒号前的数字
                unique_numbers.add(number)
    return len(unique_numbers)

# 调用函数并打印结果
filename = 'unique.txt'
unique_line_count = count_unique_lines(filename)
print(f'不重复的行数: {unique_line_count}')