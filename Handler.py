#
#   2025/10/2 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   游戏逻辑处理模块
#

class HandlerFunc:
    def __init__(self) -> None:
        self._stack = []
        self._inner_stack = []
    def push(self, func, *args):
        #self._inner_stack.append((func, args))
        self._stack.append((func, args))
    def exe_next(self):
        func_unit = self._stack.pop()
        if func_unit is not None:
            func, args = func_unit
            return func(*args)
    def is_empty(self):
        if len(self._stack) == 0:
            return True
        return False