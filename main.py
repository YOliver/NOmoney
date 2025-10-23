#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   主函数入口
#
import threading
import ThreadingLogic
import Accounting
import CardManage
import Handler
import Windows

if __name__ == "__main__":
    print("小丑牌启动...")
    Acctountor = Accounting.accountant()
    Pocker = CardManage.Cards(Acctountor)
    HandlerFunc = Handler.HandlerFunc()
    MainWin = Windows.window(Pocker, HandlerFunc)

    t_game_win = threading.Thread(target=ThreadingLogic.MainWinLogic, args=(Pocker, Acctountor, HandlerFunc, MainWin))
    t_controller_win = threading.Thread(target=ThreadingLogic.ControllerLogic, args=(Pocker, Acctountor, HandlerFunc, MainWin))
    t_log = threading.Thread(target=ThreadingLogic.Log, args=(Pocker, Acctountor))

    t_game_win.start()
    t_controller_win.start()
    t_log.start()

    t_game_win.join()
    t_controller_win.join()
    t_log.join()

    
    print("游戏结束！！！！")
