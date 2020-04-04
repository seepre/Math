from .Vector import Vector 

class Matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d] 

    def T(self):
        """返回矩阵的转置"""
        return Matrix([[e for e in self.col_vector(i)] 
                        for i in range(self.col_num())])
    
    @classmethod
    def identity(cls, n):
        """返回一个n行n列的单位矩阵"""
        m = [[0]*n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)

    def __add__(self, another):
        """矩阵加法"""
        assert self.shape() == another.shape(), \
            "Error in adding."
        return Matrix([[a + b for a, b in zip(self.row_vector(i), another.row_vector(i))] 
                        for i in range(self.row_num())])

    def __sub__(self, another):
        """矩阵减法"""
        assert self.shape() == another.shape(), \
            "Error in subtracting."
        return Matrix([[a - b for a, b in zip(self.row_vector(i), another.row_vector(i))]
                        for i in range(self.row_num())])

    def dot(self, another):
        """返回矩阵乘法的结果"""
        if isinstance(another, Vector):
            # 矩阵和向量的乘法
            assert self.col_num() == len(another), \
                "Error in Matrix-Vector Multiplication."
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])

        if isinstance(another, Matrix):
            # 矩阵和矩阵的乘法 
            assert self.col_num() == another.row_num(), \
                "Error in Matrix-Matrix Multiplication."
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num())] 
                                for i in range(self.row_num())])

    def __mul__(self, k):
        """实现矩阵数量乘法：self * k"""
        return Matrix([[e * k for e in self._values[i]] 
                        for i in range(self.row_num())])

    def __rmul__(self, k):
        """返回矩阵的数量乘结果（右乘）: k * self """
        return self * k 

    def __truediv__(self, k):
        """矩阵数量除法的结果矩阵：self / k"""
        return (1 / k) * self 

    def __pos__(self):
        """返回矩阵取正的结果"""
        return 1 * self 

    def __neg__(self):
        """返回矩阵取负的结果"""
        return -1 * self 

    def row_vector(self, index):
        """返回矩阵第index个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵的第index个列向量"""
        return Vector([row[index] for row in self._values])

    def __getitem__(self, pos):
        """返回矩阵pos位置的元素"""
        r, c = pos 
        return self._values[r][c]

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]

    def shape(self):
        """返回矩阵的形状"""
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values) 

    __str__ = __repr__ 