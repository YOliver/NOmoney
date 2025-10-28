#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   会计记账结算模块
#
import GlobData

class accountant:
    pocker_hand_no = None
    effective_cards = []
    def __init__(self) -> None:
        self.pocker_hand_no = GlobData.NONE
    # 牌型判定+基础得分
    def HandIdentification(self, cardslist): 
        if cardslist == None or len(cardslist) == 0:
            self.pocker_hand_no = GlobData.NONE
            return     
        suitledger=[0,0,0,0]
        pointledger=[0,0,0,0,0,0,0,0,0,0,0,0,0]
        for card in cardslist:
            pointledger[card.point] = pointledger[card.point] + 1
            suitledger[card.suit] = suitledger[card.suit] + 1
        pointstr = ''.join(str(x) for x in pointledger)
        if '11111' in pointstr and 5 in suitledger: # 同花顺
            self.pocker_hand_no = GlobData.STRATFLUSH
        elif '11111' in pointstr: # 顺子
            self.pocker_hand_no = GlobData.STRAT
        elif 5 in suitledger: # 同花
            self.pocker_hand_no = GlobData.FLUSH
        elif 4 in pointledger: # 四条
            self.pocker_hand_no = GlobData.FOUR
        elif 3 in pointledger and 2 in pointledger: # 葫芦
            self.pocker_hand_no = GlobData.FULLHS
        elif 3 in pointledger: # 三条
            self.pocker_hand_no = GlobData.THREE
        elif pointledger.count(2) == 2:# 两队
            self.pocker_hand_no = GlobData.TWOP
        elif 2 in pointledger: # 对子
            self.pocker_hand_no = GlobData.PAIR
        else: # 高牌
            self.pocker_hand_no = GlobData.HIGH
        self.geteffcardslist(self.pocker_hand_no, cardslist, pointledger)
    # 牌型记录变量回位
    def ResetHandNo(self):
        self.pocker_hand_no = GlobData.NONE
    # 获取牌型和统计分
    def GetTypeAndScoreStr(self):
        if self.pocker_hand_no == GlobData.NONE:
            return ""
        basic_score = GlobData.PKHADSCO[self.pocker_hand_no]
        total_score = basic_score[0]*basic_score[1]
        return GlobData.PKHADSTR[self.pocker_hand_no]+" "+str(basic_score[0])+"X"+str(basic_score[1])+"="+str(total_score)
    # 获取有效的牌列表
    def geteffcardslist(self, hand_type, cardslist, pointledger):
        if hand_type == GlobData.STRATFLUSH or hand_type == GlobData.FULLHS or hand_type == GlobData.STRAT or hand_type == GlobData.FLUSH:
            self.effective_cards = cardslist
            return
        positions = []
        if hand_type == GlobData.FOUR:
            positions = [pointledger.index(4)]
        if hand_type == GlobData.FULLHS:
            positions = [pointledger.index(3),pointledger.index(2)]
        if hand_type == GlobData.THREE:
            positions = [pointledger.index(3)]
        if hand_type == GlobData.TWOP:
            positions = [index for index, value in enumerate(pointledger) if value == 2]
        if hand_type == GlobData.PAIR:
            positions = [pointledger.index(2)]
        if hand_type == GlobData.HIGH:
            positions.append(0)
            for i in range(len(pointledger)):
                if pointledger[i] == 1:
                    positions[0] = i
        for card in cardslist:
            if card.point in positions:
                self.effective_cards.append(card)

                

