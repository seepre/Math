class Vector:
    def __init__(self, v_list):
        """使用list()复制一份，避免从外面改变values的值"""
        self._values = list(v_list)

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
    