#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   显示界面管理模块
#
import sys
import os
import GlobData

#界面大小
VERTICAL = 50
HORIZONTAL = 100
#Card大小
VCARD = 15
HCARD = 15
#点数和花色显示的行号
SUITPOINTHOR = 1

# 手牌绘制
def PaintingHandCard(Cards):
    artboard = []
    for item_card in Cards.hand:
        for j in range(VCARD):
            itemhorizontal = ""
            for i in range(HCARD):
                if j == 0 or j == VCARD - 1:
                    itemhorizontal=itemhorizontal+"+"
                else:
                    if i == 0 or i == HCARD - 1:
                        itemhorizontal=itemhorizontal+"+"
                    else:
                        itemhorizontal=itemhorizontal+" "
            # 绘制点数和花色
            if j == SUITPOINTHOR:
                strsuitpoint = GlobData.POINT[item_card.point] + GlobData.SUIT[item_card.suit]
                itemhorizontal = itemhorizontal[:2]+strsuitpoint+itemhorizontal[4:]
            # 整行拼接
            if j>=len(artboard):
                artboard.append("")
            artboard[j]=artboard[j] + " " + itemhorizontal
    
    # 界面打印
    for itemhorizontal in artboard: 
        print(itemhorizontal)

# 主界面绘制
def PaintingMainWindows(Cards):
    os.system('cls')
    PaintingHandCard(Cards)
