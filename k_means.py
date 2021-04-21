import argparse

class Cluster:
    def __init__(self, dot):
        self.center = dot
        self.N = 1

    def get_center(self):
        return self.center

      def update_center(self, dot, sign=1):
        """ center =  (center *N + dot) / N+1 """
        if self.N + sign == 0:
            print("remove the only dot - Error !!")

        f = lambda arr, num : [ele * num for ele in arr]
        tmp = f(self.center,self.N)
        dot = f(dot,sign)
        self.center = [sum(x) for x in zip(tmp,dot)]
        self.N += sign
        self.center = f(self.center, 1/self.N)


    def get_distance(self, dot, sum = 0):
        for axis in range(len(dot)):
            sum += (self.center[axis] - dot[axis]) ** 2
        return sum ** 0.5


def load_data_to_dots(filename):
    dots_list = []
    file1 = open(filename, 'r')
    Lines = file1.readlines()

    for line in Lines:
        dot = [float(word) for word in line.split(sep=",")]
        dots_list.append(dot)
    return dots_list


def get_nearest_cluster_index(dot, cluster_list):
    index_of_min_distance = 0
    min_distance = float("inf")
    for j, cluster in enumerate(cluster_list):
        d = cluster.get_distance(dot)
        if d <= min_distance:
            min_distance = d
            index_of_min_distance = j
    return index_of_min_distance


def print_outputs(dot_list):
    print("expected:")
    for dot in dot_list:
        for num in dot:
            print(num, end=",")
        print("")


def print_results(clusters):
    for cluster in clusters:
        for num in cluster.get_center():
            print("%.4f" % num, end=",")
        print("")


def kmean(k,max_iter,filename):
    #filename = "input_" + test_index + ".txt"
    """input_list =input("insert filename").split(" ")
    k=input_list.pop(0)
    max_iter = input_list.pop(0)
    input_list.remove(0)
    filename=input_list.pop(0)"""


    dot_list = load_data_to_dots(filename)
    dot_in_cluster = [-1] * len(dot_list)
    dot_should_be_at = [-1] * len(dot_list)
    clusters = []

    for i in range(k):  ## create K cluters
        clusters.append(Cluster(dot_list[i]))
        dot_in_cluster[i] = i

    iter_num = 0
    is_clsuters_changed = True
    while iter_num < max_iter and is_clsuters_changed:
        is_clsuters_changed = False

        for i, dot in enumerate(dot_list):
            dot_should_be_at[i] = get_nearest_cluster_index(dot, clusters)

        for i, dot in enumerate(dot_list):
            j = dot_should_be_at[i]
            if dot_in_cluster[i] == -1:  ## dot not in any cluster
                clusters[j].update_center(dot)
                dot_in_cluster[i] = j  # set dot i to cluster j
                is_clsuters_changed = True

            elif dot_in_cluster[i] != j:
                clusters[dot_in_cluster[i]].update_center(dot, -1)  ## remove dot from old cluster
                clusters[j].update_center(dot)
                dot_in_cluster[i] = j
                is_clsuters_changed = True

        iter_num += 1

        print(iter_num, is_clsuters_changed)

    print_results(clusters)

    print_outputs(load_data_to_dots("output_1.txt"))
