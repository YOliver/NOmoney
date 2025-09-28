#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   显示界面管理模块
#
import os
import GlobData

###PockerCard图形数据###
#长宽
VCARD = 10 # 长
HCARD = 15 # 宽
#花色点数起始行
SUITPOINTHOR = 1
#花色点数起始列
SUITPOINTVER = 1

### 小丑牌图形数据 ***

### 出牌区图形数据 ***
VTABLE = VCARD
HTABLE = HCARD*5

###信息栏###
#信息栏大小
VIB = VCARD
HIB = HCARD * 8
#牌堆信息起始行
IBHOR = 2
IBVER = 1


class window:
    artboard = []
    cards = None
    def __init__(self, cards) -> None:
        self.cards = cards
    def PaintingMainWindows(self):
        os.system('cls')
        # 信息栏
        self.PaintingCardsFrame(1, VIB, HIB)
        barstr = "牌堆：" + str(len(self.cards.deck)) + "/" + str(len(GlobData.BASIC_HAND)) + "   " + "墓地：" + str(len(self.cards.cemetery))
        self.PaintingCommonTXT(barstr, IBVER, IBHOR)
        self.Painting()
        self.CleanBoard()
        # 小丑牌&塔罗牌
        self.PaintingCardsFrame(5, VCARD, HCARD)
        JTstr = "空位"
        self.PaintingCommonTXT(JTstr, int(HCARD/2), int(VCARD/2))
        self.Painting()
        self.CleanBoard()
        # 出牌区
        self.PaintingCardsFrame(1,VTABLE, HTABLE)
        self.Painting()
        self.CleanBoard()
        # 手牌
        self.PaintingCardsFrame(len(self.cards.hand), VCARD, HCARD)
        self.PaintingCardPointSuit()
        self.Painting()
        self.CleanBoard()
    #牌框绘制        
    def PaintingCardsFrame(self, cnt, ver, hor):
        for _ in range(cnt):
            for j in range(ver):
                itemhorizontal = ""
                for i in range(hor):
                    if j == 0 or j == ver - 1:
                        itemhorizontal=itemhorizontal+"+"
                    else:
                        if i == 0 or i == hor - 1:
                            itemhorizontal=itemhorizontal+"+"
                        else:
                            itemhorizontal=itemhorizontal+" "
                if j >= len(self.artboard):
                    self.artboard.append("")
                self.artboard[j] = self.artboard[j] + itemhorizontal
    #绘制扑克牌花色和点数
    def PaintingCardPointSuit(self):
        handcardcnt = len(self.cards.hand)
        start = SUITPOINTVER - HCARD
        for i in range(handcardcnt):
            item_card = self.cards.hand[i]
            strsuitpoint = GlobData.POINT[item_card.point] + GlobData.SUIT[item_card.suit]
            start = start + HCARD
            end = start + len(strsuitpoint)
            self.artboard[SUITPOINTHOR] = self.artboard[SUITPOINTHOR][:start] + strsuitpoint + self.artboard[SUITPOINTHOR][end:]
    #打印
    def Painting(self):
        for itemhorizontal in self.artboard: 
            print(itemhorizontal) 
    #清空画板
    def CleanBoard(self):
        self.artboard=[]
    #文本信息通用绘制
    def PaintingCommonTXT(self, str, ver, hor):
        strcnt = len(str.encode('gbk'))
        self.artboard[hor] = self.artboard[hor][:ver] + str + self.artboard[hor][strcnt+ver:]
    #小丑牌&塔罗牌绘制
    def PaintingJockerTarot(self):
        pass

