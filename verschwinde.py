import os
import shutil
import time

# 定义垃圾文件的判断条件
# 这里以文件大小为例，假设小于10字节的文件被认为是垃圾文件
# 你可以根据需要调整这个条件
JUNK_FILE_SIZE_THRESHOLD = 10  # 垃圾文件的大小阈值（单位：字节）

# 定义需要清理的目录
DIRECTORY_TO_CLEAN = '/'

def remove_junk_files(directory):
    # 遍历目录中的所有文件和文件夹
    for filename in os.listdir(directory):
        # 获取文件的完整路径
        file_path = os.path.join(directory, filename)
        # 判断是否是文件
        if os.path.isfile(file_path):
            # 获取文件大小
            file_size = os.path.getsize(file_path)
            # 判断文件大小是否小于阈值
            if file_size < JUNK_FILE_SIZE_THRESHOLD:
                # 删除文件
                os.remove(file_path)
                print(f"Deleted junk file: {file_path}")

# 调用函数，开始清理垃圾文件
remove_junk_files(DIRECTORY_TO_CLEAN)
