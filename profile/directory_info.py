import json


def process_directory(directory, parent_path=""):
    # 如果 parent_path 是根目录（即 "/"），不在路径前加多余的 "/"
    current_path = f"{parent_path}{directory['name']}" if parent_path != "/" else f"/{directory['name']}"
    total_size = 0
    file_count = 0

    # 初始化存储结果的字典
    results = {}
    entries_map = {}
    entries_list = []

    for index, (name, entry) in enumerate(directory.get("entries", {}).items()):
        entries_map[name] = index
        entries_list.append(name)

        if entry['attr']['type'] == "directory":
            # 如果是子目录，递归处理
            entry['name'] = name  # 将子目录的名字保存到 entry 中
            sub_results = process_directory(entry, current_path + "/")
            # 将子目录的结果合并到最终结果中
            results.update(sub_results)
            # 累加子目录中的文件总大小和文件数量到当前目录
            total_size += sub_results[f"{current_path}/{name}"]["total_size"]
            file_count += sub_results[f"{current_path}/{name}"]["file_count"]
        elif entry['attr']['type'] == "regular":
            # 如果是文件，累加文件大小和文件数量
            total_size += entry['attr']['length']
            file_count += 1

    # 将当前目录的结果存储到字典中
    results[current_path] = {
        "inode": directory['attr']['inode'],
        "total_size": total_size,
        "file_count": file_count,
        "entries_map": entries_map,
        "entries_list": entries_list
    }

    return results


# 读取 JSON 数据
with open('athena-dump-0829.json', 'r') as file:
    data = json.load(file)

# 添加根目录的名称（假设根目录没有名称字段）
data["FSTree"]['name'] = ""

# 处理根目录
result = process_directory(data["FSTree"])


# 输出结果
# print(result)

# 如果需要保存结果到文件，可以使用以下代码
with open('directory_info.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)
