import re

# 读取文件内容
file_path = 'time.txt'  # 请根据实际路径修改
with open(file_path, 'r') as file:
    lines = file.readlines()

# 初始化变量
io_times = []
process_times = []

# 正则表达式匹配模式
io_pattern = r'IO time: ([\d\.]+)([µms]+)'
process_pattern = r'Process time: ([\d\.]+)([µms]+)'


# 将时间单位转化为微秒的函数
def convert_to_microseconds(value, unit):
    if unit == 'ms':
        return float(value) * 1000  # 毫秒转微秒
    elif unit == 'µs':
        return float(value)
    return None


# 解析每一行
for line in lines:
    io_match = re.match(io_pattern, line)
    process_match = re.match(process_pattern, line)

    if io_match:
        time_value, unit = io_match.groups()
        io_times.append(convert_to_microseconds(time_value, unit))

    if process_match:
        time_value, unit = process_match.groups()
        process_times.append(convert_to_microseconds(time_value, unit))

# 计算平均时间
average_io_time = sum(io_times) / len(io_times) if io_times else 0
average_process_time = sum(process_times) / len(process_times) if process_times else 0

print(f"平均 IO time: {average_io_time} µs")
print(f"平均 Process time: {average_process_time} µs")
