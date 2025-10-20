#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   显示界面管理模块
#
import os
import GlobData
import tkinter as tk
import time
import log

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
    handler = None
    def __init__(self, cards, handler) -> None:
        self.cards = cards
        self.handler = handler
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
        log.LoggerDebug(["结算选中牌&焦点牌", self.cards.roundplayingcardrecord, self.cards.focuscard])
        up_leng = YLONG // 2
        for i in range(handcardcnt):
            item_card = self.cards.hand[i]
            if item_card.no in self.cards.roundplayingcardrecord: # 选中牌
                for j in range(YLONG):
                    ypos = len(self.artboard)-YLONG+j
                    xpos = XLONG*i
                    ynewpos = ypos-up_leng
                    self.artboard[ynewpos] = self.artboard[ynewpos][:xpos] + self.artboard[ypos][xpos:xpos+XLONG] + self.artboard[ynewpos][xpos+XLONG:]
                    self.artboard[ypos] = self.artboard[ypos][:xpos] + " "*XLONG + self.artboard[ypos][xpos+XLONG:]
            if item_card.no == self.cards.focuscard:    # 鼠标焦点牌
                ypos = len(self.artboard)-YLONG-1
                if self.cards.focuscard in self.cards.roundplayingcardrecord:
                    ypos = ypos-up_leng
                xpos = XLONG*i
                self.artboard[ypos] = self.artboard[ypos][:xpos] + "+"*XLONG + self.artboard[ypos][xpos+XLONG:]


# 游戏操控界面
class GameController:
    PockerCards = None
    Handler = None
    MainWin = None
    def __init__(self, Pocker, Handler, MainWin) -> None:
        self.PockerCards = Pocker
        self.Handler = Handler
        self.MainWin = MainWin
        self.PockerButton = []
        self.root = tk.Tk()
        self.root.title("尹建文的小丑牌")
        self.root.geometry("1000x400")
    def PaintingController(self):
        # 创建pocker牌按钮
        self.create_dynamic_pocker_button()
        # 创建出牌按钮
        button = tk.Button(self.root, text="出牌", width=10, height=5,bg="#4CAF50",fg="white",font=('Arial', 12, 'bold'))
        button.grid(row=2, column=0)
        button.bind("<Button-1>", lambda event: self.PlayButtonClickLogic(event))
        # 创建弃牌按钮

        # 创建花色/点数排序按钮
        button = tk.Button(self.root, text="花色", width=10, height=5,bg="#4CAF50",fg="white",font=('Arial', 12, 'bold'))
        button.grid(row=2, column=2)
        button.bind("<Button-1>", lambda event: self.SortButtonClickLogic(event,GlobData.COMMAND_SORT_BY_SUIT_SIGNAL))
        button = tk.Button(self.root, text="点数", width=10, height=5,bg="#4CAF50",fg="white",font=('Arial', 12, 'bold'))
        button.grid(row=2, column=3)
        button.bind("<Button-1>", lambda event: self.SortButtonClickLogic(event,GlobData.COMMAND_SORT_BY_POINT_SIGNAL))

        self.root.mainloop()
    def create_dynamic_pocker_button(self):
        # 清理旧数据
        for button in self.PockerButton:
            button.destroy()
        self.PockerButton.clear()
        # 生成新按钮
        button_col = 0
        log.LoggerDebug(["开始生成扑克按钮", len(self.PockerCards.hand)])
        for card in self.PockerCards.hand:
            point_str = GlobData.POINT[card.point]+GlobData.SUIT[card.suit]
            button = tk.Button(self.root, text=point_str, width=10, height=5, bg="yellow", fg="black",activebackground='#45a049')
            button.grid(row=1,column=button_col, padx=10, pady=10, ipadx=5, ipady=5, sticky="nsew")   
            # 绑定鼠标事件
            pocker_number = card.no
            log.LoggerDebug(["按钮扑克绑定", pocker_number, point_str])
            button.bind("<Enter>", lambda event, num = pocker_number: self.EnterLogic(event, num))     # 鼠标进入事件[7](@ref)[8](@ref)
            button.bind("<Leave>", lambda event, num = pocker_number: self.LeaveLogic(event, num))     # 鼠标离开事件[7](@ref)[8](@ref)
            button.bind("<Button-1>", lambda event, args = pocker_number: self.PockerClickLogic(event,args))  # 鼠标左键点击事件[6](@ref)[8](@ref)

            self.PockerButton.append(button)
            button_col += 1   
    def EnterLogic(self,event, btnum): # 鼠标接触按钮
        log.LoggerDebug(["鼠标聚焦按钮：",btnum])
        self.Handler.push(self.PockerCards.MouseFocusOn,btnum)
        self.Handler.push(self.MainWin.PaintingMainWindows)
    def LeaveLogic(self,event, btnum): # 鼠标离开按钮
        self.Handler.push(self.PockerCards.MouseFocusOff)
        self.Handler.push(self.MainWin.PaintingMainWindows)
    def PockerClickLogic(self,event, args): # 鼠标点击pocker按钮
        log.LoggerDebug(["点击选中牌", args])
        self.Handler.push(self.PockerCards.ClickPocker, args)
        self.Handler.push(self.MainWin.PaintingMainWindows)
    def PlayButtonClickLogic(self, event): # 点击出牌
        self.Handler.push(self.PockerCards.PlayingCards)
    def SortButtonClickLogic(self, event, args):
        self.Handler.push(self.PockerCards.SortTypeSet, args)
        self.Handler.push(self.PockerCards.Sorting)
        self.Handler.push(self.MainWin.PaintingMainWindows)
        self.Handler.push(self.create_dynamic_pocker_button)

