#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   card管理模块
#
import GlobData
import random
import time
import log

class Card:
    def __init__(self,point,suit,buff,number) -> None:
        self.point = point
        self.suit = suit
        self.buff = buff
        self.no = number

class Cards:
    deck = []   # 牌堆
    cemetery=[] # 墓地
    hand=[]     # 手牌
    roundplayingcardrecord=[]   # 出牌区 *牌编号
    focuscard = -1  # 鼠标焦点牌
    sort_type = GlobData.COMMAND_SORT_BY_POINT_SIGNAL # 排序方式
    serial_factory = -1  #编号工厂
    def __init__(self) -> None:
        for item_card in GlobData.BASIC_HAND:
            num = self.serial_product()
            item = Card(item_card[0],item_card[1], item_card[2], num)
            self.deck.append(item)
            log.LoggerDebug(["生成牌堆：", item.no, item.point, item.suit])
    def serial_product(self):   # 生成牌的唯一编号
        self.serial_factory += 1
        return self.serial_factory
    def ShowDeck(self):#打印牌堆
        for card in self.deck:
            print(GlobData.POINT[card.point],GlobData.SUIT[card.suit],card.buff)
    def Shuffle(self):#洗牌
        cnt_deck = len(self.deck)
        for i in range(cnt_deck):
            random_integer = random.randint(0, cnt_deck-1)
            self.deck[i], self.deck[random_integer] = self.deck[random_integer], self.deck[i]
    def Licensing(self):#发牌
        cnthand = len(self.hand)
        if GlobData.BASIC_HAND_NUM <= cnthand:
            return
        for i in range(GlobData.BASIC_HAND_NUM - cnthand):
            item_card = self.deck.pop()
            self.hand.append(item_card)
        self.Sorting()
    def SortTypeSet(self, type):
        self.sort_type = type
    def Sorting(self):#排序
        if self.sort_type == GlobData.COMMAND_SORT_BY_POINT_SIGNAL:
            self.hand = sorted(self.hand, key=lambda x: (x.point, x.suit))
        if self.sort_type == GlobData.COMMAND_SORT_BY_SUIT_SIGNAL:
            self.hand = sorted(self.hand, key=lambda x: (x.suit,x.point))
    def PlayingCards(self):#出牌
        new_hand = []
        for i in range(len(self.hand)):
            if i not in self.roundplayingcardrecord:
                new_hand.append(self.hand[i])
        self.hand = new_hand
        self.cemetery.extend(self.roundplayingcardrecord)
        return True
    def MouseFocusOn(self, pockerno):# 鼠标焦点选中
        self.focuscard = pockerno
    def MouseFocusOff(self):# 鼠标焦点离开
        self.focuscard = -1
    def ClickPocker(self, pockerno): # 鼠标点击扑克牌
        pocker = pockerno
        if pocker not in self.roundplayingcardrecord:
            if len(self.roundplayingcardrecord) < 5:
                self.roundplayingcardrecord.append(pocker)
        else:
            self.roundplayingcardrecord.remove(pocker)
