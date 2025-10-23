#
#   2025/10/2 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   游戏逻辑处理模块
#

import log

class Func:
    def __init__(self, func, args) -> None:
        self.func = func
        self.args = args
        self.pre = None
        self.next= None
        self.attachfunclass = None

class HandlerFunc:
    def __init__(self) -> None:
        emptyfunc = Func(None, None)
        self.tail = emptyfunc
        self.cur = emptyfunc
    def push(self, func, *args):
        function = Func(func, args)
        self.tail.next = function
        self.tail = function
        return function
    def exe_all(self):
        # 执行函数
        while self.cur != self.tail:
            self.cur = self.cur.next
            del self.cur.pre
            func = self.cur.func
            args = self.cur.args
            if func is not None:
                data = func(*args)
                if self.cur.attachfunclass is not None:
                    self.cur.attachfunclass.args = [data]
                    self.cur.attachfunclass.pre = self.cur
                    self.cur.attachfunclass.next = self.cur.next
                    self.cur.next = self.cur.attachfunclass
                    if self.cur.attachfunclass.next is not None:
                        self.cur.attachfunclass.next.pre = self.cur.attachfunclass
                    else:
                        self.tail = self.cur.attachfunclass
    def is_empty(self):
        if self.cur == self.tail:
            return True
        return False
    def attach(self, parent_class, func_child):
        function = Func(func_child, None)
        parent_class.attachfunclass = function
        return function