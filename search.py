import os
 
def get_folder_size(folder_path):
    # 获取文件夹的总大小（字节）
    total_size = sum(os.path.getsize(os.path.join(dirpath, filename))
                     for dirpath, _, filenames in os.walk(folder_path)
                     for filename in filenames)
    return total_size
 
def convert_bytes_to_gb(size_bytes):
    # 将字节转换成GB并保留两位小数
    return size_bytes / (1024 * 1024 * 1024)
 
def main():
    folder_path = r'E:'
    total_size_bytes = get_folder_size(folder_path)
    total_size_gb = convert_bytes_to_gb(total_size_bytes)
 
    # 打印总占用空间
    print(f"该 {folder_path} 的总占用空间为: {total_size_gb:.2f} GB")
 
    # 统计并打印每个子文件夹的大小（过滤掉大小低于1GB的文件夹）
    for dirpath, dirnames, _ in os.walk(folder_path):
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdir_size_bytes = get_folder_size(subdir_path)
            if subdir_size_bytes > 1024 * 1024 * 1024:  # 大于1GB的条件
                subdir_size_gb = convert_bytes_to_gb(subdir_size_bytes)
                print(f"--其中 {subdir_path} 的总占用空间为: {subdir_size_gb:.2f} GB")
 
if __name__ == "__main__":
    main()