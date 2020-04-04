import numpy as np 

if __name__=="__main__":
    # 矩阵的创建
    A = np.array([[1,2], [3,4]])
    print(A)

    # 矩阵的属性
    print(A.shape)  # 形状
    print(A.T) # 转置

    # 获取矩阵元素 
    print(A[1,1])
    print(A[0])
    print(A[:, 0])
    print(A[1, :])

    # 矩阵的基本运算
    B = np.array([[5,6], [7,8]])
    print(A + B) 
    print(A - B) 
    print(10*A) 
    print(A * 10)
    print(A * B)  # 注意这里是将对应的元素相乘
    print(A.dot(B))

    p = np.array([10, 100]) 
    # numpy提供了向量的加法，但在矩阵的标准中是没有意义的 
    # numpy还可以将每个元素加上一个标题，这个在numpy里叫做广播
    print(A + p) 
    print(A + 1) 
    print(A.dot(p))