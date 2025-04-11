#
#   20250411 @yinjianwen@gmail.com
#   NOmoney 项目
#   主文件
#
import md5
import searchfile
import json

designer_path = "..\\ODesigner\\"
md5datafile = "md5data.json"

# 获取指定目录下面修改过的文件名单和md5值
def check_update_file(directory, md5file):
    with open(md5file, 'r', encoding='utf-8') as file:
        oldmd5data = json.load(file)  # 读取 JSON 数据

    new_md5 = {}
    files = searchfile.list_files_in_directory(directory)
    for file in files:
        msg = md5.get_file_md5(directory+file)
        if file not in oldmd5data:
            oldmd5data[file] = ""
        if msg != oldmd5data[file]:
            new_md5[file]=msg
            print(f"modified==>{file}, md5==>{msg}")
    return new_md5

def update_chosenfile_binarydata(designer_path, md5file):
    newmd5data = check_update_file(designer_path, md5file)
    with open(md5file, 'r', encoding='utf-8') as file:
        oldmd5data = json.load(file)  # 读取 JSON 数据
    for key, value in oldmd5data.items():
        if key not in newmd5data:
            newmd5data[key] = value
    with open(md5file, 'w', encoding='utf-8') as file:
        json.dump(newmd5data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    while(1):
        msg = input(">:")
        match msg:
            case 'c':
                check_update_file(designer_path, md5datafile)
            case 'u':
                update_chosenfile_binarydata(designer_path, md5datafile)
