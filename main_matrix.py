from playLA.Matrix import Matrix 
from playLA.Vector import Vector

if __name__=="__main__":
    mat = Matrix([[1,2,3,4,5],[2,3,4,5,6]])
    mat2 = Matrix([[2,3,4,5,6], [3,4,5,6,7]]) 
    print("Add: {}".format(mat + mat2))
    print("Subtract: {}".format(mat - mat2))
    print("Truediv: {}".format(mat * 4))


    matrix1 = Matrix([[1,3], [2,4]])
    matrix2 = Matrix([[0.1, 0.5, 5, 6], [0.2, 0.5, 3, 4]])
    # 对应结果应该是
    # [(1*0.1 + 3*0.2), (1*0.5 + 3*0.5), (1*5 + 1*3), (1*6 + 1*4)]
    # [(2*0.1 + 4*0.2), (2*0.5 + 4*0.5), (2*5 + 4*3), (2*6 + 4*4)]
    print("matrix1 dot(matrix2) = {}".format(matrix1.dot(matrix2)))
    vec = Vector([1,3])
    # 矩阵乘向量结果
    # [(1*1 + 3*3), (1*2 + 3 * 4)]
    print("matrix1 dot(vec)={}".format(matrix1.dot(vec)))
