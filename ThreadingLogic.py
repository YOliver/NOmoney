#
#   2025/10/2 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   线程逻辑管理模块
#

import Windows
import GlobData
import time

def MainWinLogic(PockerClass, AcctountorClass):
    PockerCards = PockerClass
    Acctountor = AcctountorClass
    MainWin = Windows.window(PockerCards)

    PockerCards.Shuffle()
    while True:
        PockerCards.Licensing()
        while True:
            if GlobData.COMMOND_PLAYCARD_SINGAL == True:
                PockerCards.PlayingCards()
                print(Acctountor.ScoreBill())
                GlobData.COMMOND_PLAYCARD_SINGAL = False
            MainWin.PaintingMainWindows()
            GlobData.COMMOND_REFRESH_SINGAL = False
            while GlobData.COMMOND_REFRESH_SINGAL == False:
                time.sleep(0.1) 


def ControllerLogic(PockerClass, AcctountorClass):
    Controller = Windows.GameController(PockerClass)
    Controller.PaintingController()
