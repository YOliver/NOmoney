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
import CMDTool


class window:
    cards = None
    handler = None
    tool = None
    infor_bar = []
    jocker_bar = []
    table_bar = []
    hand_bar = []
    def __init__(self, cards, handler) -> None:
        self.cards = cards
        self.handler = handler
        self.tool = CMDTool.CMDtool()
    def PaintingMainWindows(self):
        # 信息栏
        self.PaintingInformationBar()
        # 小丑牌&塔罗牌
        self.PaintingJockerTarot()
        # 出牌区
        self.PaintingTableErea()
        # 手牌
        self.PaintingHandCards()
        self.Painting()
    #打印
    def Painting(self):
        os.system('cls')
        self.tool.Spraying(self.infor_bar)
        self.tool.Spraying(self.jocker_bar)
        self.tool.Spraying(self.table_bar)
        self.tool.Spraying(self.hand_bar)
    # 信息栏绘制
    def PaintingInformationBar(self):
        self.infor_bar = self.tool.PaintFrame(1, CMDTool.YIBLONG, CMDTool.XIBLONG, "+", " ")
        game_str = "尹建文的小丑牌"
        self.tool.PaintComTXT(game_str, (CMDTool.XIBLONG-self.tool.CalculationLength(game_str))//2, 1, self.infor_bar)
        desk_str = "牌堆：" + str(len(self.cards.deck)) + "/" + str(len(GlobData.BASIC_HAND)) + "   " + "墓地：" + str(len(self.cards.cemetery))
        self.tool.PaintComTXT(desk_str, 2, 2, self.infor_bar)
        log.LoggerDebug(["当前牌型：", self.cards.Acctountor.pocker_hand_no])
        if self.cards.Acctountor.pocker_hand_no != GlobData.NONE:
            self.tool.PaintComTXT("牌型："+GlobData.PKHADSTR[self.cards.Acctountor.pocker_hand_no], 2, 3, self.infor_bar)
    #小丑牌&塔罗牌绘制
    def PaintingJockerTarot(self):
        self.jocker_bar = self.tool.PaintFrame(1, CMDTool.YEXTRAEREALONG, CMDTool.XLONG*5, " ", " ")
        jocker_erea = self.tool.PaintFrame(5, CMDTool.YLONG, CMDTool.XLONG, "+", " ")
        self.tool.AlterBoard(None, None, jocker_erea, self.jocker_bar)
    #出牌区绘制
    def PaintingTableErea(self):
        if len(self.cards.roundplayingcardrecord) > 0:
            self.table_bar = self.tool.PaintPockerCards("+", " ", self.cards.roundplayingcardrecord)
        else:
            self.table_bar = self.tool.PaintFrame(1, CMDTool.YLONG, CMDTool.XLONG*8, " ", " ")
    #手牌区绘制
    def PaintingHandCards(self):
        self.hand_bar = self.tool.PaintFrame(1, CMDTool.YEXTRAEREALONG, CMDTool.XLONG*len(self.cards.hand), " ", " ")
        cards_erea = self.tool.PaintPockerCards("+", " ", self.cards.hand)
        self.tool.AlterBoard(None, None, cards_erea, self.hand_bar)
        # 鼠标选中牌向上弹出,焦点牌上边加粗
        log.LoggerDebug(["结算选中牌&焦点牌", self.cards.roundplayingcardcache, self.cards.focuscard])
        self.tool.AlterHandCardsBoard(self.cards.hand, self.cards.roundplayingcardcache, self.cards.focuscard, self.hand_bar)


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
        # 创建花色/点数排序按钮
        button = tk.Button(self.root, text="花色", width=10, height=5,bg="#4CAF50",fg="white",font=('Arial', 12, 'bold'))
        button.grid(row=2, column=2)
        button.bind("<Button-1>", lambda event: self.SortButtonClickLogic(event,GlobData.COMMAND_SORT_BY_SUIT_SIGNAL))
        button = tk.Button(self.root, text="点数", width=10, height=5,bg="#4CAF50",fg="white",font=('Arial', 12, 'bold'))
        button.grid(row=2, column=3)
        button.bind("<Button-1>", lambda event: self.SortButtonClickLogic(event,GlobData.COMMAND_SORT_BY_POINT_SIGNAL))
        # 创建弃牌按钮
        button = tk.Button(self.root, text="弃牌", width=10, height=5,bg="#4CAF50",fg="white",font=('Arial', 12, 'bold'))
        button.grid(row=2, column=5)
        button.bind("<Button-1>", lambda event: self.FoldButtonClickLogic(event))

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
        self.Handler.push(self.MainWin.PaintingHandCards)
        self.Handler.push(self.MainWin.Painting)
    def LeaveLogic(self,event, btnum): # 鼠标离开按钮
        self.Handler.push(self.PockerCards.MouseFocusOff)
        self.Handler.push(self.MainWin.PaintingHandCards)
        self.Handler.push(self.MainWin.Painting)
    def PockerClickLogic(self,event, args): # 鼠标点击pocker按钮
        log.LoggerDebug(["点击选中牌", args])
        self.Handler.push(self.PockerCards.ClickPocker, args)
        f = self.Handler.push(self.PockerCards.GetCardByNo)
        self.Handler.attach(f, self.PockerCards.Acctountor.HandIdentification)
        self.Handler.push(self.MainWin.PaintingHandCards)
        self.Handler.push(self.MainWin.PaintingInformationBar)
        self.Handler.push(self.MainWin.Painting)
    def PlayButtonClickLogic(self, event): # 点击出牌
        self.Handler.push(self.PockerCards.PlayingCards)
    def SortButtonClickLogic(self, event, args): # 排序
        self.Handler.push(self.PockerCards.SortTypeSet, args)
        self.Handler.push(self.PockerCards.Sorting)
        self.Handler.push(self.MainWin.PaintingHandCards)
        self.Handler.push(self.MainWin.Painting)
        self.Handler.push(self.create_dynamic_pocker_button)
    def FoldButtonClickLogic(self, event): # 弃牌
        self.Handler.push(self.PockerCards.LaunchCards)
        self.Handler.push(self.PockerCards.Acctountor.ResetHandNo)
        self.Handler.push(self.MainWin.PaintingHandCards)
        self.Handler.push(self.MainWin.PaintingTableErea)
        self.Handler.push(self.MainWin.PaintingInformationBar)
        self.Handler.push(self.MainWin.Painting)
        self.Handler.push(time.sleep(1))
        self.Handler.push(self.PockerCards.PlaceInCemetery)
        self.Handler.push(self.PockerCards.Licensing)
        self.Handler.push(self.MainWin.PaintingHandCards)
        self.Handler.push(self.MainWin.PaintingTableErea)
        self.Handler.push(self.MainWin.Painting)
        self.Handler.push(self.create_dynamic_pocker_button)
