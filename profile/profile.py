import json
from tqdm import tqdm

# 4MB 块的大小
CHUNK_SIZE = 4 * 1024 * 1024

# 定义一个结构体类，用于存储 ObjectName 和 Length 的配对列表
class ChunkInfo:
    def __init__(self, chunk_list):
        self.chunk_list = chunk_list  # 存储 (ObjectName, Length) 的配对列表

# 处理 chunks 中的每个 slice
def process_chunks(chunks):
    processed_chunks = []
    for chunk_index, chunk in enumerate(chunks):
        for i, slice_ in enumerate(chunk["slices"]):
            if slice_["id"] == 0:
                # 如果 id 为 0，表示取消掉上一项
                if processed_chunks:
                    processed_chunks.pop()
            else:
                slice_id = slice_["id"]
                total_size = slice_["size"]
                pos = slice_.get("pos", 0)  # 获取 pos 属性，如果没有则默认为 0
                slice_chunks = []

                current_pos = pos
                slice_part_index = 0
                next_pos = slice_.get("pos", 0)
                while total_size > 0:
                    current_slice_size = min(CHUNK_SIZE, total_size)
                    next_pos += current_slice_size

                    # 生成 objectName，使用原始大小
                    object_name = f"jfs/chunks/{slice_id // 1000000}/{slice_id // 1000}/{slice_id}_{slice_part_index}_{current_slice_size}"

                    # 处理规约的大小
                    length = current_slice_size  # 初始长度为块大小

                    # 如果存在下一个 slice，且下一个 slice 的 pos 比当前更小，进行规约
                    if i < len(chunk["slices"]) - 1:
                        next_slice = chunk["slices"][i + 1]
                        next_slice_pos = next_slice.get("pos", 0)
                        if next_slice_pos < next_pos:
                            overlap = next_pos - next_slice_pos
                            length -= overlap

                    # 生成 (ObjectName, Length) 的配对
                    slice_chunk = {
                        "ObjectName": object_name,
                        "Length": length  # 使用修正后的长度
                    }
                    slice_chunks.append(slice_chunk)

                    # 更新状态
                    total_size -= current_slice_size
                    current_pos += current_slice_size
                    slice_part_index += 1

                processed_chunks.extend(slice_chunks)
    return processed_chunks


# 递归函数用于遍历 FSTree 并提取 inode、路径、类型、大小和 chunks 信息
def extract_inodes_and_paths(node, current_path="", progress_bar=None):
    inodes_paths = []
    total_size = 0

    # 如果当前节点有 entries，那么递归遍历其子项
    if "entries" in node:
        for entry_name, entry_node in node["entries"].items():
            new_path = f"{current_path}/{entry_name}"
            sub_inodes_paths, sub_total_size = extract_inodes_and_paths(entry_node, new_path, progress_bar)
            inodes_paths.extend(sub_inodes_paths)
            total_size += sub_total_size  # 将子项的大小累加到当前目录

    # 检查当前节点是否有属性(attr)，并且是否是文件或目录
    if "attr" in node:
        inode = node["attr"]["inode"]
        node_type = node["attr"]["type"]
        node_size = node["attr"]["length"]
        node_chunks = node.get("chunks", [])

        # 如果是文件，直接记录大小并处理 chunks
        if node_type == "regular":
            total_size += node_size
            processed_chunks = process_chunks(node_chunks)

            # 将 (ObjectName, Length) 配对存入 ChunkInfo 结构体
            chunk_info = ChunkInfo(processed_chunks)
        else:
            processed_chunks = []
            chunk_info = None

        # 在所有子项处理完毕后，记录当前目录或文件的信息，包括处理后的 chunks
        inodes_paths.append((inode, current_path, node_type, total_size, chunk_info))

    # 每处理完一个节点，更新进度条
    if progress_bar:
        progress_bar.update(1)

    return inodes_paths, total_size


# 从 JSON 文件读取数据
with open('athena-dump.json', 'r') as file:
    data = json.load(file)

# 计算需要处理的总节点数
total_nodes = sum(1 for _ in extract_inodes_and_paths(data.get('FSTree', {}))[0])

# 创建进度条
with tqdm(total=total_nodes, desc="Processing") as progress_bar:
    # 提取 FSTree 中的 inode、路径、类型、大小和 chunks 信息
    fstree = data.get('FSTree', {})
    inodes_and_paths, _ = extract_inodes_and_paths(fstree, progress_bar=progress_bar)

# 将结果存储到一个文件中
with open('inodes_paths.txt', 'w') as output_file:
    for inode, path, node_type, node_size, chunk_info in inodes_and_paths:
        output_file.write(f"Inode: {inode}, Path: {path}, Type: {node_type}, Size: {node_size}\n")
        if chunk_info:
            output_file.write("  Chunks:\n")
            for chunk in chunk_info.chunk_list:
                output_file.write(f"    ObjectName: {chunk['ObjectName']}, Length: {chunk['Length']}\n")

print("Inode、路径、类型、大小和 chunks 信息已存储到 inodes_paths.txt 文件中。")
