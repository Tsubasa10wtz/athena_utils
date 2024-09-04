import re

import matplotlib.pyplot as plt

# 假设文件名为 'data1.txt' 和 'data2.txt'
file = 'data1.txt'

# 读取文件内容
def read_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        id, times = line.split(':')
        start, end = times.split(' - ')
        data.append((int(id), float(start), float(end)))
    return data

data = read_file(file)


batches = []
batch = []
flag = 0
previous_id = None
for entry in data:
    current_id = entry[0]
    if previous_id is not None:
        if current_id != previous_id:
            flag += 1
    else:
        flag += 1
    if flag > 64:
        batches.append(batch)
        batch = []
        flag = 1
    batch.append((float(entry[1]), float(entry[2])))
    previous_id = current_id

# 计算每个batch的近似IO+Transform时间
batch_times = []
for batch in batches:
    if batch:
        start_time = batch[0][0]
        end_time = batch[-1][1]
        batch_times.append((start_time, end_time))

file2 = 'data2.txt'


# 解析第二个文件
def parse_file2(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    iter_data = []
    current_iter = {}

    for line in lines:
        if "finish iter" in line:
            # 当检测到新的迭代时，存储上一个迭代的数据并初始化新的字典
            if current_iter:
                iter_data.append(current_iter)
                current_iter = {}
        elif "cal time" in line:
            # 使用正则表达式提取计算时间的开始和结束时间戳
            cal_times = re.findall(r"cal time: (\d+\.\d+) - (\d+\.\d+)", line)
            if cal_times:
                # cal_times[0] 是一个包含两个字符串（开始和结束时间戳）的元组
                start_time, end_time = map(float, cal_times[0])
                current_iter['cal_time'] = (start_time, end_time)
        elif "read time" in line:
            # 提取读取时间
            read_time = re.search(r"read time: ([\d\.]+)", line)
            if read_time:
                current_iter['read_time'] = float(read_time.group(1))
        elif "transform time" in line:
            # 提取转换时间
            transform_time = re.search(r"transform time: ([\d\.]+)", line)
            if transform_time:
                current_iter['transform_time'] = float(transform_time.group(1))

    # 添加最后一个迭代的数据
    if current_iter:
        iter_data.append(current_iter)

    return iter_data


# 解析文件并存储数据
iter_data = parse_file2(file2)

print(iter_data)

min_length = min(len(batch_times), len(iter_data))
batche_times = batch_times[:min_length]
iter_data = iter_data[:min_length]

def normalize_times(batches, iter_data):
    # 找到所有时间戳中的最小值
    min_time = min([b[0] for b in batches] + [item['cal_time'][0] for item in iter_data])

    # 规范化batches时间
    normalized_batches = [(start - min_time, end - min_time) for start, end in batches]

    # 规范化iter_data中的计算时间
    for item in iter_data:
        cal_start, cal_end = item['cal_time']
        item['cal_time'] = (cal_start - min_time, cal_end - min_time)

    return normalized_batches, iter_data

batch_times, iter_data = normalize_times(batch_times, iter_data)

def plot_gantt(batches, iter_data):
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 分别代表 read, transform, calc
    labels = ['Read Time', 'Transform Time', 'Compute Time']

    # plt.style.use("fivethirtyeight")
    plt.rcParams.update({'font.size': 30})

    yticks = []
    yticklabels = []
    fig, ax = plt.subplots(figsize=(10, 8))

    for i, (batch_time, iter) in enumerate(zip(batches, iter_data)):
        # 计算整个batch的持续时间
        total_duration = batch_time[1] - batch_time[0]

        # 读取时间和转换时间的比例
        read_time = iter['read_time']
        transform_time = iter['transform_time']
        total_process_time = read_time + transform_time

        # 按比例计算时间区间
        read_duration = total_duration * (read_time / total_process_time)
        transform_duration = total_duration * (transform_time / total_process_time)

        # 定义时间区间
        read_start = batch_time[0]
        read_end = read_start + read_duration
        transform_start = read_end
        transform_end = transform_start + transform_duration
        calc_start = float(iter['cal_time'][0])
        calc_end = float(iter['cal_time'][1])

        # 添加到图中
        ax.broken_barh([(read_start, read_duration)], (i * 3, 1), facecolors=colors[0], edgecolor='black')
        ax.broken_barh([(transform_start, transform_duration)], (i * 3, 1), facecolors=colors[1], edgecolor='black')
        ax.broken_barh([(calc_start, calc_end - calc_start)], (i * 3, 1), facecolors=colors[2], edgecolor='black')

        yticks.append(i * 3 + 0.5)
        yticklabels.append(f"{i+1}")

    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel("Mini Batches")
    ax.set_yticks(yticks[::2])  # 只保留每两个的刻度
    ax.set_yticklabels(yticklabels[::2])  # 只显示每两个的标签
    ax.tick_params(axis='x')
    ax.set_xlim(left=0)  # 设置横轴从0开始
    # ax.set_title('Timeline Of Batches')


    # 添加图例
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=colors[i], edgecolor='black', label=labels[i]) for i in range(3)]
    ax.legend(handles=legend_elements, loc='lower right')
    plt.tight_layout()

    plt.savefig("./gantt.pdf", format='pdf', bbox_inches='tight')
    plt.show()



# 调用绘图函数
plot_gantt(batch_times, iter_data)