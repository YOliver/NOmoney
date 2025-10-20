#
#   2025/10/2 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   游戏逻辑处理模块
#

class Func:
    def __init__(self, func, args) -> None:
        self.func = func
        self.args = args
        self.pre = None
        self.next= None

class HandlerFunc:
    def __init__(self) -> None:
        emptyfunc = Func(None, None)
        self.tail = emptyfunc
        self.cur = emptyfunc
        self.head = emptyfunc
    def push(self, func, *args):
        function = Func(func, args)
        self.tail.next = function
        self.tail = function
    def exe_all(self):
        # 执行函数
        while self.cur != self.tail:
            self.cur = self.cur.next
            func = self.cur.func
            args = self.cur.args
            if func is not None:
                func(*args)
        # 清理已经处理的函数
        while self.head != self.cur:
            tmp = self.head.next
            del self.head
            self.head = tmp
    def is_empty(self):
        if self.cur == self.tail:
            return True
        return False
