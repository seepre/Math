import math
from ._globals import EPSILON

class Vector:
    def __init__(self, v_list):
        """使用list()复制一份，避免从外面改变values的值"""
        self._values = list(v_list)

    @classmethod
    def zero(cls, dim):
        return Vector([0] * dim)

    def norm(self):
        """返回向量的模
            sqrt（）表示开平方
            sqrt(v1**2 + v2**2 + v3**2)
        """
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        """返回向量的单位向量"""
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error!")
        # 需要实现truediv魔术方法才能使用除法
        return Vector(self._values) / self.norm()

    def dot(self, another):
        """向量的点乘"""
        assert len(self) == len(another), \
            "Error in dot, Length of vctors must be same."
        return sum(a * b for a, b in zip(self, another))

    def __add__(self, another):
        """实现加法运算"""
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        # return Vector([a + b] for a, b in zip(self._values, another._values))
        # 这里直接使用self和another是因为重载了__iter__魔术方法
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        """实现减法运算"""
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        """向量乘以K"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """返回数量乘法的结果向量: k * self"""
        return self * k 

    def __truediv__(self, k):
        """返回数量除法的结果向量"""
        return (1 / k) * self 

    def __pos__(self):
        """取正值"""
        return 1 * self

    def __neg__(self):
        """取负值"""
        return -1 * self 

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __iter__(self):
        """返回迭代器"""
        return self._values.__iter__()
    
    def __repr__(self):
        return "Vector({})".format(self._values)
    
    def __str__(self):
        return "({})".format(", ".join(str(i) for i in self))
    