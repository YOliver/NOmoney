#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   card管理模块
#
import GlobData
import random
import Windows

class Card:
    def __init__(self,point,suit,buff) -> None:
        self.point = point
        self.suit = suit
        self.buff = buff

class Cards:
    deck = []
    cemetery=[]
    hand=[]
    roundplayingcardrecord=[]
    focuscard = -1
    def __init__(self) -> None:
        for item_card in GlobData.BASIC_HAND:
            item = Card(item_card[0],item_card[1], item_card[2])
            self.deck.append(item)
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
    def Sorting(self, sorttype):#排序
        if sorttype == GlobData.SORTFORPOINT:
            self.hand = sorted(self.hand, key=lambda x: (x.point, x.suit))
        if sorttype == GlobData.SORTFORSUIT:
            self.hand = sorted(self.hand, key=lambda x: (x.suit,x.point))
    def PlayingCards(self, playingcardslist):#出牌
        if len(playingcardslist) > len(self.hand):
            return False
        self.roundplayingcardrecord = []
        new_hand = []
        for i in range(len(self.hand)):
            if any(x == i for x in playingcardslist):
                self.roundplayingcardrecord.append(self.hand[i])
            else:
                new_hand.append(self.hand[i])
        self.hand = new_hand
        self.cemetery.extend(self.roundplayingcardrecord)
        return True
