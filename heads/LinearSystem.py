from .Matrix import Matrix
from .Vector import Vector 

class LinearSystem:
    def __init__(self, A, b):
        """ A表示矩阵，b表示方程结果的列向量 """
        assert A.row_num() == len(b), "Row number of A must be equal to the length of b"
        self._m = A.row_num() # 矩阵的行数
        self._n = A.col_num() # 矩阵的列数
        assert self._m == self._n  # TODO 
        
        # 创建增广矩阵 
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                    for i in range(self._m)]

   

    def _max_row(self, index, n):
        best, ret = abs(self.Ab[index][index]), index 
        for a in range(index + 1, n):
            if abs(self.Ab[a][index]) > best:
                best, ret = abs(self.Ab[index][index]), index
        return ret 

    def _forward(self):
        n = self._m 
        for i in range(n):
            # Ab[i][i]为主元
            max_row = self._max_row(i, n)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            # 将主元变成1
            self.Ab[i] = self.Ab[i] / self.Ab[i][i] # TODO 处理分母为0的情况
            for j in range(i + 1, n):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i] 

    def _backward(self):
        n = self._m 
        for i in range(n - 1, -1, -1):
            # Ab[i][i]为主元
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    def gauss_jordan_elimination(self):
        """高斯消元"""
        self._forward()
        self._backward()

    def echo(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])