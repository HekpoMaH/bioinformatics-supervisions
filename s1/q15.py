from pprint import pprint
class Node:
    def __init__(self, s):
        self.species = s
        self.right = None
        self.left = None
        self.dist_left = 0
        self.dist_right = 0
        self.age = 0

def D_avg(D, cluster1, cluster2):
    dist = .0
    n = len(cluster1.species)
    m = len(cluster2.species)
    for s1 in cluster1.species:
        for s2 in cluster2.species:
            dist += D[s1][s2]
    return dist / (n * m)

# assume species are indexed 0 to n-1
def upgma(D):
    
    nodes = []
    n = len(D)
    for i in range(n):
        node = Node([i])
        nodes = nodes +[node]

    nc = n
    while nc > 1:
        c1 = 0; c2 = 0; i1 = 0; i2 = 0
        min_dis = float("inf")
        for i in range(nc):
            for j in range(i+1, nc):
                dis = D_avg(D, nodes[i], nodes[j])
                if dis < min_dis:
                    c1 = nodes[i]; c2 = nodes[j]
                    i1 = i; i2 =j
                    min_dis = dis
        node = Node(c1.species + c2.species)
        node.age = D_avg(D, c1, c2) / 2.0
        node.left = c1; node.right = c2;
        node.dist_left = node.age - c1.age
        node.dist_right = node.age - c2.age

        new_nodes = []
        for i in range(nc):
            if i != i1 and i != i2:
                new_nodes = new_nodes + [nodes[i]]

        new_nodes = new_nodes + [node]
        nodes = new_nodes[:]
        nc = nc -1

    return nodes[0]

def dump(node, level=0):
    if node == None:
        return
    print(' ' * level,"Cluster contains:",node.species)
    if node.left != None:
        print(' ' * level,
            "Distance to left is {:f} and right is {:f}".format(node.dist_left, node.dist_right))
    print()
    dump(node.left, level+3)
    dump(node.right, level+3)

D1 = [[0, 3, 4, 4, 4],
      [3, 0, 4, 4, 4],
      [4, 4, 0, 1, 2],
      [4, 4, 1, 0, 2],
      [4, 4, 2, 2, 0]]

D2 = [[0, 5, 7, 10],
      [5, 0, 4, 7 ],
      [7, 4, 0, 5 ],
      [10,7, 5, 0 ]]
dump(upgma(D1))
print("__________________________________________")
print()
dump(upgma(D2))
