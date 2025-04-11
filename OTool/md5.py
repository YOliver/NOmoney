#
#   20250411 @yinjianwen@gmail.com
#   NOmoney 项目
#   获取指定文件得MD5值,以来windows系统的cmd指令
#
import subprocess

def get_file_md5(file_path):
    try:
        # 调用 certutil 命令
        result = subprocess.run(['certutil', '-hashfile', file_path, 'MD5'], 
                                capture_output=True, text=True, check=True)
        
        # certutil 输出的结果中，MD5 值在第二行
        md5_value = result.stdout.splitlines()[1].strip()
        return md5_value
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
    except IndexError:
        print("无法获取 MD5 值，输出格式可能不正确。")
    except Exception as e:
        print(f"发生错误: {e}")
