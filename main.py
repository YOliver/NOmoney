#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   主函数入口
#
import GlobData
import CardManage
import windows

if __name__ == "__main__":
    print("小丑牌启动...")
    Cards = CardManage.Cards()
    Cards.Shuffle()
    while True:
        Cards.Licensing()
        Cards.Sorting(GlobData.SORTFORPOINT)
        playing_card = False
        while playing_card == False:
            windows.PaintingMainWindows(Cards)
            print("你的操作>:")
            arg = input().split()
            button = arg[0]
            if button == 'a': #按指定顺序暂时手牌
                Cards.Sorting(int(arg[1]))
            if button == 'b': #出牌
                Cards.PlayingCards(list(map(int, arg[1:])))
                playing_card = True