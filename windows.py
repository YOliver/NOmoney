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
        # 鼠标选中牌向上弹出,焦点牌上边加粗
        up_leng = YLONG // 2
        for ichosen in self.cards.roundplayingcardrecord: # 选中牌
            for j in range(YLONG):
                ypos = len(self.artboard)-YLONG+j
                xpos = XLONG*ichosen
                ynewpos = ypos-up_leng
                self.artboard[ynewpos] = self.artboard[ynewpos][:xpos] + self.artboard[ypos][xpos:xpos+XLONG] + self.artboard[ynewpos][xpos+XLONG:]
                self.artboard[ypos] = self.artboard[ypos][:xpos] + " "*XLONG + self.artboard[ypos][xpos+XLONG:]
        if self.cards.focuscard > -1:   # 鼠标焦点牌
            ypos = len(self.artboard)-YLONG-1
            if self.cards.focuscard in self.cards.roundplayingcardrecord:
                ypos = ypos-up_leng
            xpos = XLONG*self.cards.focuscard
            self.artboard[ypos] = self.artboard[ypos][:xpos] + "+"*XLONG + self.artboard[ypos][xpos+XLONG:]


# 游戏操控界面
class GameController:
    PockerCards = None
    def __init__(self, Pocker) -> None:
        self.PockerCards = Pocker
    def PaintingController(self):
        root = tk.Tk()
        root.title("小丑牌")
        root.geometry("1000x400")
        # 创建pocker牌按钮
        for i in range(8):
            button = tk.Button(root, text=str(i), width=10, height=5, bg="yellow", fg="black",activebackground='#45a049')
            button.grid(row=1,column=i, padx=10, pady=10, ipadx=5, ipady=5, sticky="nsew")            
            # 绑定鼠标事件
            button.bind("<Enter>", self.EnterLogic)    # 鼠标进入事件[7](@ref)[8](@ref)
            button.bind("<Leave>", self.LeaveLogic)    # 鼠标离开事件[7](@ref)[8](@ref)
            button.bind("<Button-1>", lambda event: self.ClickLogic(event,i)) # 鼠标左键点击事件[6](@ref)[8](@ref)
        # 创建出牌按钮
        button = tk.Button(root, text="出牌", width=10, height=5,bg="#4CAF50",fg="white",font=('Arial', 12, 'bold'))
        button.grid(row=2, column=0)
        button.bind("<Button-1>", lambda event: self.ClickLogic(event,GlobData.COMMOND_PLAYCARD))
        # 创建弃牌按钮

        # 创建花色/点数排序按钮
        button = tk.Button(root, text="花色", width=10, height=5,bg="#4CAF50",fg="white",font=('Arial', 12, 'bold'))
        button.grid(row=2, column=2)
        button.bind("<Button-1>", lambda event: self.ClickLogic(event,GlobData.COMMOND_SORT_SUIT))
        button = tk.Button(root, text="点数", width=10, height=5,bg="#4CAF50",fg="white",font=('Arial', 12, 'bold'))
        button.grid(row=2, column=3)
        button.bind("<Button-1>", lambda event: self.ClickLogic(event,GlobData.COMMOND_SORT_POINT))

        root.mainloop()
    def EnterLogic(self,event): # 鼠标接触按钮
        self.PockerCards.focuscard = int(event.widget['text'])
        GlobData.COMMOND_REFRESH_SINGAL = True
    def LeaveLogic(self,event): # 鼠标离开按钮
        self.PockerCards.focuscard = -1
        GlobData.COMMOND_REFRESH_SINGAL = True
    def ClickLogic(self,event, btnum): # 鼠标点击按钮
        GlobData.COMMOND_REFRESH_SINGAL = True
        if btnum < GlobData.COMMOND_PLAYCARD:   # 选中扑克牌
            chosencardslength = len(self.PockerCards.roundplayingcardrecord)
            ichosen = int(event.widget['text'])
            if ichosen not in self.PockerCards.roundplayingcardrecord:
                if chosencardslength < 5:
                    self.PockerCards.roundplayingcardrecord.append(ichosen)
            else:
                self.PockerCards.roundplayingcardrecord.remove(ichosen)
        if btnum == GlobData.COMMOND_PLAYCARD: # 出牌
            GlobData.COMMOND_PLAYCARD_SINGAL = True
        if btnum == GlobData.COMMOND_SORT_POINT or GlobData.COMMOND_SORT_SUIT: # 排序
            self.PockerCards.sort_type = btnum
            GlobData.COMMOND_SORT_SINGAL = True

