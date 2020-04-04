from heads.Vector import Vector

if __name__ == "__main__":
    vc = Vector([34,55])
    vc2 = Vector([2, 10])
    
    print("{} + {} = {}".format(vc, vc2, vc + vc2))
    print("{} + {} = {}".format(vc, vc2, vc - vc2))
    print("{} + {} + {}".format(vc, 4, vc * 4))
    print("{}, {}".format(-vc, -vc2))
    
    zero = Vector.zero(2)
    print("{}".format(zero))

    print("{} + {} = {}".format(vc, zero, vc + zero))

    print("{} => {}".format(vc, str(vc.norm())))

    normalize = vc.normalize()
    print("{} => {}".format(vc, normalize))

    print("{}".format(normalize.norm()))

    try:
        print("{}".format(zero.normalize()))
    except  ZeroDivisionError:
        print("Canno tnormalize zero.")


    print("{} * {} = {}".format(vc, vc2, vc.dot(vc2)))