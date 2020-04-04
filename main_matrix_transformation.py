from heads.Matrix import Matrix 
from heads.Vector import Vector 
import matplotlib.pyplot as plt 
import math 

if __name__=="__main__":
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]

    x = [point[0] for point in points] 
    y = [point[1] for point in points] 

    # 坐标系配置
    plt.figure(figsize=(5, 5))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y) 

    # 创建原始矩阵
    P = Matrix(points)

    # 创建计算矩阵
    # 缩放
    #T = Matrix([[2, 0], [0, 1.5]])
    # X轴翻转
    #T = Matrix([[1, 0], [0, -1]]) 
    # Y轴翻转
    #T = Matrix([[-1, 0], [0, 1]])
    # 原点翻转
    #T = Matrix([[-1, 0], [0, -1]])
    # X辆错切
    #T = Matrix([[1, 0.5], [0, 1]])
    # Y轴错切
    #T = Matrix([[1, 0], [0.5, 1]])

    # 以原点旋转
    theta = math.pi / 3  # 60度角
    T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

    P2 = T.dot(P.T()) # 转置 
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
                [P2.col_vector(i)[1] for i in range(P2.col_num())])

    plt.show()