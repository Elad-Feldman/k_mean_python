import  k_means as km
import argparse

def tests():
    """v1 = [3,600,"1"]
    v2 = [7,200,"2"]
    v3 = [15,300,"3"]
    V = []
    V.append(v1)
    V.append(v2)
    V.append(v3)
    for v in V:
        print("========run test: ",v[2],"===========")
        print(v)"""
    parser = argparse.ArgumentParser()
    parser.add_argument("k_num", help="k", type=int)

    parser.add_argument("max_iter", help="max iteration",type=int)
    args = parser.parse_args()
    k = args.k_num
    max_iter = args.max_iter

    #filename = input("insert file name")
    filename="input_1.txt"
    km.kmean(k,max_iter,filename)

tests()
