import copy
def dist(data_point, center):
    # doesn't matter if we minimize sqrt(x) or just x
    return (data_point[0] - center[0])**2.0 + (data_point[1] - center[1])**2.0
def d(data_point, centers):
    min = 1e9
    for x in centers:
        if dist(data_point, x) < min:
            min = dist(data_point, x)
    return min

def farthest_first_traversal(data, k):
    centers = [data[0]]
    visited = {data[0]}
    while len(centers) < k:
        data_point = None
        distance = 0
        for p in data:
            if p not in visited:
                if d(p, centers) > distance:
                    distance = d(p, centers)
                    data_point = p
        assert(data_point != None)
        visited.add(copy.deepcopy(data_point))
        centers.append(copy.deepcopy(data_point))
    return centers

print(farthest_first_traversal([(1,1), (1,10), (2,10), (2,9), (5,5), (6,6), (6,5)], 3))
