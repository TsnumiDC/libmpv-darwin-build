import os
import shutil

# 设定当前工作目录（可根据需要自行调整）
current_directory = os.getcwd()

# 目标文件夹名称
header_directory = os.path.join(current_directory, 'headers')

# 如果目标文件夹不存在，创建它
if not os.path.exists(header_directory):
    os.makedirs(header_directory)

# 遍历当前目录的所有文件
for filename in os.listdir(current_directory):
    # 检查文件是否是一个头文件
    if filename.endswith('.h'):
        # 源文件的完整路径
        source_path = os.path.join(current_directory, filename)
        # 目标文件的完整路径
        destination_path = os.path.join(header_directory, filename)
        # 复制文件
        shutil.copy(source_path, destination_path)
        print(f"Copied '{filename}' to '{header_directory}'.")

print("Completed copying .h files to headers directory.")