from datetime import datetime

# 定义筛选时间
filter_time = "2024/11/27 22:15:00"  # 替换为你想筛选的时间
filter_time_obj = datetime.strptime(filter_time, "%Y/%m/%d %H:%M:%S")

# 打开日志文件并读取内容
with open('read.log', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# 筛选出时间晚于指定时间的记录
filtered_lines = []
for line in lines:
    # 提取日志中的时间部分
    log_time_str = line.split()[0] + " " + line.split()[1]  # 获取日期和时间
    log_time_obj = datetime.strptime(log_time_str, "%Y/%m/%d %H:%M:%S")

    # 如果日志的时间晚于筛选时间，则将该行加入到筛选结果中
    if log_time_obj > filter_time_obj:
        filtered_lines.append(line)

# 将筛选后的结果保存到一个新文件
with open('filtered_log.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(filtered_lines)

print(f"筛选后的日志已保存到 'filtered_log.txt'")
