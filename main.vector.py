from playLA.Vector import Vector

if __name__ == "__main__":
    vc = Vector([34,55])
    vc2 = Vector([2, 10])
    
    print("{} + {} = {}".format(vc, vc2, vc + vc2))
    print("{} + {} = {}".format(vc, vc2, vc - vc2))
    print("{} + {} + {}".format(vc, 4, vc * 4))
    print("{}, {}".format(-vc, -vc2))
    