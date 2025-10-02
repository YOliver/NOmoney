#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   显示界面管理模块
#
import os
import GlobData
import tkinter as tk
import time

###PockerCard图形数据###
#长宽
XLONG = 10 # 宽
YLONG = 10 # 长
#花色点数起始行列
XSUITPOINT = 1
YSUITPOINT = 1

### 小丑牌图形数据 ***

### 出牌区图形数据 ***
XTABLELONG = XLONG*10
YTABLELONG = YLONG + 2

###信息栏###
#信息栏大小
XIBLONG = XLONG * 8
YIBLONG = YLONG



class window:
    artboard = []
    cards = None
    def __init__(self, cards) -> None:
        self.cards = cards
    def PaintingMainWindows(self):
        os.system('cls')
        # 信息栏
        self.PaintingInformationBar()
        # 小丑牌&塔罗牌
        self.PaintingJockerTarot()
        # 出牌区
        self.PaintingTableErea()
        # 手牌
        self.PaintingHandCards()
        self.Painting()
        self.CleanBoard()
    #牌框绘制        
    def PaintingCardsFrame(self, cnt, ylong, xlong, FrameChar, PaddingChar):
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
        self.artboard.extend(BoardThisTime)
    #打印
    def Painting(self):
        for itemhorizontal in self.artboard: 
            print(itemhorizontal) 
    #清空画板
    def CleanBoard(self):
        self.artboard=[]
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
    #文本信息通用绘制
    def PaintingCommonTXT(self, str, x, y):
        strcnt = self.CalculationLength(str)
        self.artboard[y] = self.artboard[y][:x] + str + self.artboard[y][strcnt+x:]
    # 信息栏绘制
    def PaintingInformationBar(self):
        self.PaintingCardsFrame(1, YIBLONG, XIBLONG, "+", " ")
        barstr = "牌堆：" + str(len(self.cards.deck)) + "/" + str(len(GlobData.BASIC_HAND)) + "   " + "墓地：" + str(len(self.cards.cemetery))
        self.PaintingCommonTXT(barstr, 2, 2)
    #小丑牌&塔罗牌绘制
    def PaintingJockerTarot(self):
        self.PaintingCardsFrame(5, YLONG, XLONG, "+", " ")
    #出牌区绘制
    def PaintingTableErea(self):
        self.PaintingCardsFrame(1, YTABLELONG, XTABLELONG, " ", " ")
    #手牌区绘制
    def PaintingHandCards(self):
        self.PaintingCardsFrame(len(self.cards.hand), YLONG, XLONG, "+", " ")
        handcardcnt = len(self.cards.hand)
        xstart = XSUITPOINT - YLONG
        ypos = len(self.artboard) - (YLONG-YSUITPOINT)
        for i in range(handcardcnt):
            item_card = self.cards.hand[i]
            strsuitpoint = GlobData.POINT[item_card.point] + GlobData.SUIT[item_card.suit]
            xstart = xstart + YLONG
            self.PaintingCommonTXT(strsuitpoint, xstart, ypos)
        # 鼠标焦点牌/选中牌向上弹出
        up_leng = YLONG // 2
        up_display_card_list = GlobData.CHOSENPOCKERLIST
        if GlobData.MOUNSEFOCUS not in GlobData.CHOSENPOCKERLIST:
            up_display_card_list = GlobData.CHOSENPOCKERLIST + [GlobData.MOUNSEFOCUS]
        for ichosen in up_display_card_list:
            if ichosen < 0:
                continue
            for j in range(YLONG):#把选中的牌挑选出来,向上显示
                ypos = len(self.artboard)-YLONG+j
                xpos = XLONG*ichosen
                ynewpos = ypos-up_leng
                self.artboard[ynewpos] = self.artboard[ynewpos][:xpos] + self.artboard[ypos][xpos:xpos+XLONG] + self.artboard[ynewpos][xpos+XLONG:]
                self.artboard[ypos] = self.artboard[ypos][:xpos] + " "*XLONG + self.artboard[ypos][xpos+XLONG:]
        
# 游戏操控界面
class GameController:
    def __init__(self) -> None:
        pass
    def PaintingController(self):
        root = tk.Tk()
        root.title("小丑牌")
        root.geometry("600x400")
        # 创建pocker牌按钮
        for i in range(8):
            button = tk.Button(root, text=str(i), bg="yellow", fg="black",activebackground='#45a049')
            button.grid(row=1,column=i, padx=10, pady=10, ipadx=5, ipady=5, sticky="nsew")            
            # 绑定鼠标事件
            button.bind("<Enter>", self.EnterLogic)    # 鼠标进入事件[7](@ref)[8](@ref)
            button.bind("<Leave>", self.LeaveLogic)    # 鼠标离开事件[7](@ref)[8](@ref)
            button.bind("<Button-1>", self.ClickLogic) # 鼠标左键点击事件[6](@ref)[8](@ref)

        root.mainloop()
    def EnterLogic(self,event): # 鼠标接触按钮
        GlobData.MOUNSEFOCUS = int(event.widget['text'])
        GlobData.REFRESH = True
    def LeaveLogic(self,event): # 鼠标离开按钮
        GlobData.MOUNSEFOCUS = -1
        GlobData.REFRESH = True
    def ClickLogic(self,event): # 鼠标点击按钮
        chosencardslength = len(GlobData.CHOSENPOCKERLIST)
        ichosen = int(event.widget['text'])
        if ichosen not in GlobData.CHOSENPOCKERLIST:
            if chosencardslength < 5:
                GlobData.CHOSENPOCKERLIST.append(ichosen)
        else:
            GlobData.CHOSENPOCKERLIST.remove(ichosen)