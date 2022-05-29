print(__file__)
from model import *
import math


def summary(l):
    ans = l[0]
    for item in l[1:]:
        ans += item
    return ans


class power(vector):
    #物理定义，力
    def __init__(self, m, d) -> None:
        self.magnitude = m
        self.direction = d


class velocity(vector):
    #物理定义，速度
    def diff(self):
        passs


class motion(vector):
    #物理定义，加速度
    pass


class struct:
    #物体的抽象
    def __init__(self) -> None:
        self.position = coordinate(0, 0, 0) #位置
        self.force    = []                  #受力
        self.speed    = velocity()          #速度
        self.mass     = 0                   #质量

    def next(self, time):
        all_force = summary(self.force)

        net_amoti = motion()
        net_amoti.magnitude = all_force.magnitude / self.mass
        net_amoti.direction = all_force.direction

        net_v = net_amoti * time

        net_s = ( self.speed + net_v ) * ( time / 2 )