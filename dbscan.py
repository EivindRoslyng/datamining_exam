import numpy as np
from sklearn.cluster import DBSCAN
data =  np.array([[3, 1], [2,2], [3,2], [4,2], [2,3], [4,3], [3, 4], [5,4], [3,6], [2,7], [5,5], [6,5], [7,5], [8,5], [6,6], [7,6], [5,8], [6,7], [7,7]])


def distance(point, list):
    newlist = []
    for elememt in list:
        newlist.append(manhattan_distance(point, elememt))
    return newlist


def manhattan_distance(a, b):
    return np.abs(a - b).sum()


def corepoint (point, data, eps, minpts):
    array =  len([x for x in distance(point, data) if x <= eps])
    if array >= minpts:
        return True
    else:
        return False

def density_connected (point1, point2, data, eps , minpts):
    clustering = DBSCAN(eps=eps, min_samples=minpts).fit(data)
    data_list = data.tolist()
    labels = clustering.labels_
    point1index = data_list.index(point1)
    point2index = data_list.index(point2)
    label1point = labels[point1index]
    label2point = labels[point2index]
    if ((label1point and label2point) !=-1 and label1point == label2point  ) :
        return True
    else:
        return False

def directly_density_reachable(point1, point2, data, eps , minpts):
    point1 = np.array(point1)
    point2 = np.array(point2)
    if corepoint(point2, data, eps, minpts) and manhattan_distance(point1, point2)<= eps:
        return True
    else:
        return False

def density_reachable(point1, point2, data, eps , minpts):
    clustering = DBSCAN(eps=eps, min_samples=minpts).fit(data)
    data_list = data.tolist()
    labels = clustering.labels_
    point1index = data_list.index(point1)
    point2index = data_list.index(point2)
    label1point = labels[point1index]
    label2point = labels[point2index]
    if (corepoint(point2, data, eps, minpts) and label1point == label2point):
        return True
    else:
        return False


print(density_reachable([5,8],[6,7], data, 2, 4))



