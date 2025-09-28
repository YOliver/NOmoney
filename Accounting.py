#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   会计记账结算模块
#
import GlobData

class accountant:
    cards = None
    pockerhands = None
    def __init__(self, cards) -> None:
        self.cards = cards
    def ScoreBill(self):
        self.pockerhands = self.__HandTypeScore()

    ### 会计内部工具 ###
    def __HandTypeScore(self): # 牌型判定
        suitledger=[0,0,0,0]
        pointledger=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        for item_card in self.cards.roundplayingcardrecord:
            suitledger[item_card.suit] = suitledger[item_card.suit] + 1
            pointledger[item_card.point] = pointledger[item_card.point] + 1
        pockerhands = GlobData.HIGH #高牌
        if 5 in suitledger:#同花
            pockerhands = GlobData.FLUSH
        straightmark = 0
        for i in pointledger:
            if i == 4:#四条
                pockerhands = GlobData.FOUR
                break
            if i == 3:
                if pockerhands == GlobData.PAIR: # 葫芦
                    pockerhands = GlobData.FULLHS
                    break
                else:#三条
                    pockerhands = GlobData.THREE if GlobData.THREE > pockerhands else pockerhands
            if i == 2:
                if pockerhands == GlobData.THREE:#葫芦
                    pockerhands = GlobData.FULLHS
                    break
                elif pockerhands == GlobData.PAIR:#两对
                    pockerhands = GlobData.TWOP if GlobData.TWOP > pockerhands else pockerhands
                else:#对子
                    pockerhands = GlobData.PAIR if GlobData.PAIR > pockerhands else pockerhands
            if i == 1 and straightmark >= 0:
                straightmark = straightmark + 1
                if straightmark == 5 and pockerhands == GlobData.FLUSH:#同花顺
                    pockerhands = GlobData.STRATFLUSH
            if i == 0 and straightmark > 0 and straightmark < 5:
                straightmark = -1
        return pockerhands