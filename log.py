#
#   2025/10/2 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   日志模块
#
import time

log_txt_path = ".\\LOG\\"
__private_txt_cache__ = []
__cache_lock__ = False

def log_secretary():
    while True:
        txt_name = "jocker_pocker_"+time.strftime('%Y-%m-%d-%H', time.localtime())+".log"
        log_file = open(log_txt_path+txt_name, 'w', encoding='utf-8')
        hour = time.localtime().tm_hour
        while True:
            if len(__private_txt_cache__) > 0:
                __cache_lock__ = True # 写日志，先锁上
                formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                for item in __private_txt_cache__:
                    log_file.write(formatted_time + " DEBUG " + item + "\n")
                __cache_lock__ = False # 写完日志，解锁
            if hour != time.localtime().tm_hour:
                log_file.close()
                break
            time.sleep(0.1)

def LoggerDebug(txt):
    while __cache_lock__ == True:
        time.sleep(0.1)
    __cache_lock__ == True
    __private_txt_cache__.append(str(txt))
    __cache_lock__ == False

