from heads.Vector import Vector

if __name__ == "__main__":
    vc = Vector([34,55])
    vc2 = Vector([2, 10])
    # 向量加法运算
    print("{} + {} = {}".format(vc, vc2, vc + vc2))
    # 向量减法运算
    print("{} + {} = {}".format(vc, vc2, vc - vc2))
    # 向量标题乘法运算
    print("{} + {} + {}".format(vc, 4, vc * 4))
    # 向量取负
    print("{}, {}".format(-vc, -vc2))
    
    # 创建0向量
    zero = Vector.zero(2)
    print("{}".format(zero))

    # 0向量加法运算
    print("{} + {} = {}".format(vc, zero, vc + zero))

    # 求模 
    print("{} => {}".format(vc, str(vc.norm())))

    # 单位向量
    normalize = vc.normalize()
    print("{} => {}".format(vc, normalize))

    print("{}".format(normalize.norm()))

    try:
        print("{}".format(zero.normalize()))
    except  ZeroDivisionError:
        print("Canno tnormalize zero.")


    print("{} * {} = {}".format(vc, vc2, vc.dot(vc2)))