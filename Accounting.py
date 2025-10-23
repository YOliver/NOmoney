#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   会计记账结算模块
#
import GlobData

class accountant:
    pocker_hand_no = None
    def __init__(self) -> None:
        self.pocker_hand_no = GlobData.NONE
    # 牌型判定
    def HandIdentification(self, cardslist): 
        if cardslist == None or len(cardslist) == 0:
            self.pocker_hand_no = GlobData.NONE
            return
        suitledger=[0,0,0,0]
        pointledger=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        for item_card in cardslist:
            suitledger[item_card.suit] = suitledger[item_card.suit] + 1
            pointledger[item_card.point] = pointledger[item_card.point] + 1
        self.pocker_hand_no = GlobData.HIGH #高牌
        if 5 in suitledger:#同花
            self.pocker_hand_no = GlobData.FLUSH
        straightmark = 0
        for i in pointledger:
            if i == 4:#四条
                self.pocker_hand_no = GlobData.FOUR
                break
            if i == 3:
                if self.pocker_hand_no == GlobData.PAIR: # 葫芦
                    self.pocker_hand_no = GlobData.FULLHS
                    break
                else:#三条
                    self.pocker_hand_no = GlobData.THREE if GlobData.THREE > self.pocker_hand_no else self.pocker_hand_no
            if i == 2:
                if self.pocker_hand_no == GlobData.THREE:#葫芦
                    self.pocker_hand_no = GlobData.FULLHS
                    break
                elif self.pocker_hand_no == GlobData.PAIR:#两对
                    self.pocker_hand_no = GlobData.TWOP if GlobData.TWOP > self.pocker_hand_no else self.pocker_hand_no
                else:#对子
                    self.pocker_hand_no = GlobData.PAIR if GlobData.PAIR > self.pocker_hand_no else self.pocker_hand_no
            if i == 1 and straightmark >= 0:
                straightmark = straightmark + 1
                if straightmark == 5 and self.pocker_hand_no == GlobData.FLUSH:#同花顺
                    self.pocker_hand_no = GlobData.STRATFLUSH
            if i == 0 and straightmark > 0 and straightmark < 5:
                straightmark = -1
    # 牌型记录变量回位
    def ResetHandNo(self):
        self.pocker_hand_no = GlobData.NONE