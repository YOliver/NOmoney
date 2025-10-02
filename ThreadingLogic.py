#
#   2025/10/2 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   线程逻辑管理模块
#

import CardManage
import Windows
import Accounting

def MainWinLogic():
    PockerCards = CardManage.Cards()
    Act = Accounting.accountant(PockerCards)
    MainWin = Windows.window(PockerCards)

    PockerCards.Shuffle()
    while True:
        PockerCards.Licensing()
        playing_card = False
        while playing_card == False:
            MainWin.PaintingMainWindows()
            print("你的操作>:")
            arg = input().split()
            button = arg[0]
            if button == 'a': #按指定顺序暂时手牌
                PockerCards.Sorting(int(arg[1]))
            if button == 'b': #出牌
                PockerCards.PlayingCards(list(map(int, arg[1:])))
                Act.ScoreBill()
                playing_card = True


def ControllerLogic():
    Controller = Windows.GameController()
    Controller.PaintingController()
