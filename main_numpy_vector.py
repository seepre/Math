import numpy as np 

if __name__=="__main__":
    # 向量类的创建
    vec = np.array([1,2,3]) 
    print(vec)

    # 向量的创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 100))

    # 向量类的基本属性及使用
    print("size =", vec.size)
    print("size =", len(vec))
    print(vec[0])
    print(vec[-1])
    print(vec[0: 2])
    print(type(vec[0: 2]))

    # 基本运算
    vec2 = np.array([3,4,5])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec, 2 * vec))
    # 这个返回的是一个向量
    print("{} * {} = {}".format(vec, vec2, vec * vec2))
    # 这个是点乘，返回一个标量
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))
    # 求模
    print(np.linalg.norm(vec))
    # 求单位向量
    print(vec / np.linalg.norm(vec))
    # 求单位向量的模
    print(np.linalg.norm(vec / np.linalg.norm(vec)))