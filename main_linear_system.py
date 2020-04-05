from heads.Matrix import Matrix 
from heads.Vector import Vector 
from heads.LinearSystem import LinearSystem 
from heads.LinearSystem import inv

if __name__=="__main__":
    A  = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.echo()

    A2 = Matrix([[1, -3, 5], [2, -1, -3], [3, 1, 4]])
    b2 = Vector([-9, 19, -13])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.echo()
    print()
    # [2, -3, -4]

    A3 = Matrix([[1, 2, -2], [2, -3, 1], [3, -1, 3]])
    b3 = Vector([6, -10, -16])
    ls3 = LinearSystem(A3, b3)
    ls3.gauss_jordan_elimination()
    ls3.echo()
    print()
    # [-2, 1, -3]

    A4 = Matrix([[3, 1, -2], [5, -3, 10], [7, 4, 16]])
    b4 = Vector([4, 32, 13])
    ls4 = LinearSystem(A4, b4)
    ls4.gauss_jordan_elimination()
    ls4.echo()
    print()
    # [3, -4, 0.5]

    A5 = Matrix([[6, -3, 2], [5, 1, 12], [8, 5, 1]])
    b5 = Vector([31, 36, 11])
    ls5 = LinearSystem(A5, b5)
    ls5.gauss_jordan_elimination()
    ls5.echo()
    print()
    # [3, -3, 2]

    A6 = Matrix([[1, 1, 1], [1, -1, -1], [2, 1, 5]])
    b6 = Vector([3, -1, 8])
    ls6 = LinearSystem(A6, b6)
    ls6.gauss_jordan_elimination()
    ls6.echo()
    print()
    # [1, 1, 1]

    A7 = Matrix([[1, -1, 2, 0, 3],
                 [-1, 1, 0, 2, -5],
                 [1, -1, 4, 2, 4],
                 [-2, 2, -5, -1, -3]])
    b7 = Vector([1, 5, 13, -1])
    ls7 = LinearSystem(A7, b7)
    ls7.gauss_jordan_elimination()
    ls7.echo()
    print()

    A8 = Matrix([[2, 2],
                 [2, 1],
                 [1, 2]])
    b8 = Vector([3, 2.5, 7])
    ls8 = LinearSystem(A8, b8)
    if not ls8.gauss_jordan_elimination():
        print("No Solution!")
    ls8.echo()
    print()

    A9 = Matrix([[2, 0, 1],
                 [-1, -1, -2],
                 [-3, 0, 1]])
    b9 = Vector([1, 0, 0])
    ls9 = LinearSystem(A9, b9)
    if not ls9.gauss_jordan_elimination():
        print("No Solution!")
    ls9.echo()
    print()

    print("========================求逆矩阵====================")
    # 求逆向矩阵
    A = Matrix([[1, 2], [3, 4]])
    invA = inv(A)
    print(invA)
    print(A.dot(invA)) # 是一个单位矩阵
    print(invA.dot(A)) # 是一个单位矩阵
