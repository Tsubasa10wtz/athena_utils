from datetime import datetime

# 定义筛选时间
filter_time = "2024/12/21 15:16:00"
filter_time_obj = datetime.strptime(filter_time, "%Y/%m/%d %H:%M:%S")

# 定义筛选关键字
filter_keyword = "Read Fuse"

# 打开日志文件逐行处理并保存结果
with open('triviaqa_diskann_1221.log', 'r', encoding='utf-8') as infile, open('filtered_triviaqa_diskann_1221.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        try:
            # 提取日志时间
            log_time_str = line.split()[0] + " " + line.split()[1]
            log_time_obj = datetime.strptime(log_time_str, "%Y/%m/%d %H:%M:%S")

            # 判断时间和关键字是否符合条件
            if log_time_obj > filter_time_obj and filter_keyword in line:
                outfile.write(line)
        except (IndexError, ValueError):
            continue  # 跳过异常行

print("筛选后的日志已保存到 'filtered_triviaqa_diskann.txt'")