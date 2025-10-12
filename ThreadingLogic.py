#
#   2025/10/2 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   线程逻辑管理模块
#

import CardManage
import Windows
import Accounting
import GlobData
import time

def MainWinLogic():
    PockerCards = CardManage.Cards()
    Act = Accounting.accountant(PockerCards)
    MainWin = Windows.window(PockerCards)

    PockerCards.Shuffle()
    while True:
        PockerCards.Licensing()
        while True:
            if GlobData.PLAYINGCARD == True:
                PockerCards.PlayingCards()
                print(Act.ScoreBill())
                GlobData.PLAYINGCARD = False
            MainWin.PaintingMainWindows()
            GlobData.REFRESH = False
            while GlobData.REFRESH == False:
                time.sleep(0.1) 


def ControllerLogic():
    Controller = Windows.GameController()
    Controller.PaintingController()
