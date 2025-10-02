#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   主函数入口
#
import threading
import ThreadingLogic

if __name__ == "__main__":
    print("小丑牌启动...")
    t_game_win = threading.Thread(target=ThreadingLogic.MainWinLogic)
    t_controller_win = threading.Thread(target=ThreadingLogic.ControllerLogic)

    t_game_win.start()
    t_controller_win.start()

    t_game_win.join()
    t_controller_win.join()

    print("游戏结束！！！！")
