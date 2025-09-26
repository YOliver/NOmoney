#
#   20250411 @yinjianwen@gmail.com
#   NOmoney 项目
#   搜索文件
#
import os

# 输出目录下面所有文件
def list_files_in_directory(directory):
    try:
        filelist = []
        # 列出目录下的所有文件
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):  # 检查是否是文件
                filelist.append(file)
        return filelist
    except Exception as e:
        print(f"发生错误: {e}")
