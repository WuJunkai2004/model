print(__file__)

import math
import re
# xyq759026@163.com


def maybe(value):
    s = str(value)
    p = r'00000.+'
    n = re.sub(p, '', s)
    print(n)
    return eval(n)


class xyz:
    #数学定义，xyz
    def __init__(self, x:int, y:int, z:int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return '( {}, {}, {} )'.format(self.x,self.y,self.z)

    def __repr__(self) -> str:
        return self.__str__()    


class coordinate(xyz):
    #数学定义，坐标
    pass


class radians:
    #数学定义，弧度
    def __init__(self, value) -> None:
        self.value = value

    def set(self, value) -> None:
        self.value = value

    def cos(self) -> float:
        return math.cos(self.value)

    def sin(self) -> float:
        return math.sin(self.value)

    def tan(self) -> float:
        return math.tan(self.value)

    def __str__(self) -> str:
        return '{} rad'.format(self.value)


class degrees:
    #数学定义，角度
    def __init__(self, value) -> None:
        self.value = value

    def set(self, value) -> None:
        self.value = value

    def cos(self) -> float:
        return math.cos(math.radians(self.value))

    def sin(self) -> float:
        return math.sin(math.radians(self.value))

    def tan(self) -> float:
        return math.tan(math.radians(self.value))

    def __str__(self) -> str:
        return '{}°'.format(self.value)


class directing(dict):
    #数学定义，空间方向
    #采用 x,y,z定义
    __all__ = ['x','y','z']
    def __init__(self, x:int, y:int, z:int) -> None:
        self['x'], self['y'], self['z'] = x, y, z
        self['base'] = [0, 0, 0]
        self._std()

    def __getattr__(self, __name: str):
        return self[__name]

    def __setattr__(self, __name: str, __value: int):
        if(__name in 'xyz'):
            self[__name] = __value
            self._std()

    def _std(self):
        v = math.sqrt(self['x']**2 + self['y']**2 + self['z']**2)
        if(v):
            self['base'] = [self['x']/v, self['y']/v, self['z']/v]

    def __str__(self) -> str:
        return '( {}, {}, {} )\n( {}, {}, {} )'.format(self['x'], self['y'], self['z'], *self['base'])

    def __repr__(self) -> str:
        return self.__str__()


class vector:
    #数学定义，矢量
    def __init__(self, long = 0, dire = directing(0,0,0) ) -> None:
        self.magnitude = long                  # 矢量的大小
        if(type(dire) == list or type(dire) == tuple):
            self.direction = directing( *dire )
        else:
            self.direction = dire                  # 矢量的方向

    def __add__(self,add):
        ans = vector()

        ans.direction = directing(
            self.magnitude * self.direction['base'][0] + add.magnitude * add.direction['base'][0],
            self.magnitude * self.direction['base'][1] + add.magnitude * add.direction['base'][1],
            self.magnitude * self.direction['base'][2] + add.magnitude * add.direction['base'][2]
            )
        ans.magnitude   = math.sqrt(ans.direction.x**2 + ans.direction.y**2 + ans.direction.z**2)

        return ans

    def __mul__(self, value):
        ans = vector()
        ans.direction = directing( *self.direction['base'] )
        ans.magnitude = self.magnitude * value
        return ans

    def __str__(self) -> str:
        return "length: {}\ndirection: {}".format(self.magnitude, self.direction)

    def __repr__(self) -> str:
        return self.__str__()
