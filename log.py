#
#   2025/10/2 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   日志模块
#
import time

log_txt_path = ".\\LOG\\"
private_txt_cache = []
cache_lock = False

def log_secretary():
    global private_txt_cache
    global cache_lock
    while True:
        txt_name = "jocker_pocker_"+time.strftime('%Y-%m-%d-%H', time.localtime())+".log"
        log_file = open(log_txt_path+txt_name, 'w', encoding='utf-8')
        hour = time.localtime().tm_hour
        while True:
            if len(private_txt_cache) > 0:
                while cache_lock == True:
                    time.sleep(0.1)
                cache_lock = True # 写日志，先锁上
                formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                for item in private_txt_cache:
                    log_file.write(formatted_time + " DEBUG " + item + "\n")
                log_file.flush()
                private_txt_cache = []
                cache_lock = False # 写完日志，解锁
            if hour != time.localtime().tm_hour:
                log_file.close()
                break
            time.sleep(1)

def LoggerDebug(txt):
    global private_txt_cache
    global cache_lock
    while cache_lock == True:
        time.sleep(0.1)
    cache_lock == True
    private_txt_cache.append(str(txt))
    cache_lock == False

