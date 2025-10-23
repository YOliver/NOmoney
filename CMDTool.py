#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   显示界面管理模块-CMD显示子模块
#
import GlobData

###PockerCard图形数据###
#卡片基本长宽
XLONG = 10 # 宽
YLONG = 10 # 长
# pocker花色点数起始行列
XSUITPOINT = 1
YSUITPOINT = 1
# 选中卡牌向上突出长度
YCHOSENUPLONG = 2
# 区域上部预留空间
YEXTRAEREALONG = YCHOSENUPLONG+2

### 信息栏 ###
#信息栏大小
XIBLONG = XLONG * 8
YIBLONG = YLONG


# 主界面绘图工具
class CMDtool:
    def __init__(self) -> None:
        pass
    #牌框绘制  
    def PaintFrame(self, cnt, ylong, xlong, FrameChar, PaddingChar):
        BoardThisTime = []
        for _ in range(cnt):
            for j in range(ylong):
                itemhorizontal = ""
                for i in range(xlong):
                    if j == 0 or j == ylong - 1:
                        itemhorizontal=itemhorizontal+FrameChar
                    else:
                        if i == 0 or i == xlong - 1:
                            itemhorizontal=itemhorizontal+FrameChar
                        else:
                            itemhorizontal=itemhorizontal+PaddingChar
                if j >= len(BoardThisTime):
                    BoardThisTime.append("")
                BoardThisTime[j] = BoardThisTime[j] + itemhorizontal
        return BoardThisTime
    # 字符串长度
    def CalculationLength(self, thestr):
        strcnt = 0
        for c in thestr:
            code = ord(c)
            if (0x4E00 <= code <= 0x9FA5) or (0x3400 <= code <= 0x4DBF) or (0x3000 <= code <= 0x303F) or (0xFF00 <= code <= 0xFFEF):
                strcnt += 2
            else:
                strcnt += 1
        return strcnt
    # 文本信息绘制
    def PaintComTXT(self, str, x, y, target):
        strcnt = self.CalculationLength(str)
        target[y] = target[y][:x] + str + target[y][strcnt+x:]
    # 画板区域整体替换
    def AlterBoard(self, ypos, ylong, newscreen, target):
        if ypos == None:
            target.extend(newscreen)
        else:
            target[ypos:ypos+ylong] = newscreen
    # 批量卡牌绘制
    def PaintPockerCards(self, FrameChar, PaddingChar, cardslist):
        erea = self.PaintFrame(len(cardslist), YLONG, XLONG, FrameChar, PaddingChar)
        ypos = YSUITPOINT
        xpos = XSUITPOINT - XLONG
        for card in cardslist:
            xpos = xpos+XLONG
            suit_point_str = GlobData.POINT[card.point] + GlobData.SUIT[card.suit]
            self.PaintComTXT(suit_point_str, xpos, ypos, erea)
        return erea
    # 涂改画板中卡牌的内容
    def AlterHandCardsBoard(self, cardslist, chosenlist, focus, target):
        for i in range(len(cardslist)):
            card = cardslist[i]
            if card.no in chosenlist:   # 选中牌
                xpos = XLONG*i
                for j in range(YLONG):
                    ypos = YEXTRAEREALONG + j
                    ynewpos = ypos - YCHOSENUPLONG
                    target[ynewpos] = target[ynewpos][:xpos]+target[ypos][xpos:xpos+XLONG]+target[ynewpos][xpos+XLONG:]
                    target[ypos] = target[ypos][:xpos]+" "*XLONG+target[ypos][xpos+XLONG:]
            if card.no == focus:    # 焦点牌
                ypos = YEXTRAEREALONG - 1
                if focus in chosenlist:
                    ypos = ypos - YCHOSENUPLONG
                xpos = XLONG*i
                target[ypos] = target[ypos][:xpos]+"+"*XLONG+target[ypos][xpos+XLONG:]
    def Spraying(self, artboard):
        for hang in artboard:
            print(hang)