import  k_means as km

def tests():
    v1 = [3,600,"1"]
    v2 = [7,200,"2"]
    v3 = [15,300,"3"]
    V = []
    V.append(v1)
    V.append(v2)
    V.append(v3)
    for v in V:
        print("========run test: ",v[2],"===========")
        print(v)
        km.kmean(v[0],v[1],v[2])

tests()
