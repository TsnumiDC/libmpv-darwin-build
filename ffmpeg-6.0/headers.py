import os
import shutil
import sys

def copy_header_files(source_directory):
    # 目标文件夹名称
    header_directory = os.path.join(source_directory, 'headers')

    # 如果目标文件夹不存在，创建它
    if not os.path.exists(header_directory):
        os.makedirs(header_directory)

    # 记录文件复制数量
    file_count = 0

    # 遍历指定目录的所有文件
    for root, dirs, files in os.walk(source_directory):
        for filename in files:
            # 检查文件是否是一个头文件
            if filename.endswith('.h'):
                # 源文件的完整路径
                source_path = os.path.join(root, filename)
                # 目标文件的完整路径
                destination_path = os.path.join(header_directory, filename)
                # 复制文件
                shutil.copy(source_path, destination_path)
                file_count += 1
                print(f"Copied '{filename}' to '{header_directory}'.")

    if file_count == 0:
        print("No .h files found.")
    else:
        print(f"Completed copying {file_count} .h files to headers directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python copy_headers.py <source_directory>")
        sys.exit(1)

    input_path = sys.argv[1]

    # 检查输入路径是否存在
    if not os.path.exists(input_path):
        print(f"Error: The path '{input_path}' does not exist.")
        sys.exit(1)

    # 执行复制操作
    copy_header_files(input_path)