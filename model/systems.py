print(__file__)
from model import *
import math

class model:
    def __init__(self) -> None:
        self.struction = []     #系统中的物体
        self.time_flow = 1      #无事件时的时间流逝速度
        self.jingdu    = 0.001  #精度
        
        self.this      = []     #此时的物质状态
        self.midd      = []     #处于中间时刻的物质状态
                                #用于二分
        self.next      = []     #下次的物质状态

        self.EQU       = []     #临界条件

    def start(self):
        while(True):
            pass
