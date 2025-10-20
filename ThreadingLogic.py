#
#   2025/10/2 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   线程逻辑管理模块
#

import Windows
import GlobData
import time
import log

def MainWinLogic(PockerClass, AcctountorClass, HandlerClass, MainWinClass):
    HandlerClass.push(PockerClass.Shuffle)
    HandlerClass.push(PockerClass.Licensing)
    HandlerClass.push(MainWinClass.PaintingMainWindows)
    while True:
        HandlerClass.exe_all()
        time.sleep(0.1)

def ControllerLogic(PockerClass, AcctountorClass, HandlerClass, MainWinClass):
    time.sleep(0.5)
    Controller = Windows.GameController(PockerClass, HandlerClass, MainWinClass)
    Controller.PaintingController()

def Log(PockerClass, AcctountorClass):
    log.log_secretary()