import numpy as np
from sklearn.neighbors import LocalOutlierFactor


data = [[1,7], [3,4], [3,7], [4,6 ] , [4,7], [5,2], [5,5], [6,6]]

def distance(point, list):
    newlist = []
    for elememt in list:
        newlist.append(manhattan_distance(point, elememt))
    return newlist


def manhattan_distance(a, b):
    return np.abs(a - b).sum()


def get_knn_score(data, neighbours_left):
    return (data[neighbours_left])



def localoutlierscore(data):
    clf = LocalOutlierFactor(n_neighbors=2, p=1)
    clf.fit_predict(data)
    print(clf.negative_outlier_factor_)





def knn(data, neigbors, points):
   data = np.array(data)
   listofpoints = []
   for point in data:
         listofpoints.append(get_knn_score(sorted(distance(point, data)), neigbors))
   for point in points:
        index = data.tolist().index(point[1:])
        print(point[:1], "is",  listofpoints[index])

points = [["A",5,2], ["B",1,7], ["D", 6,6]]

knn(data, 2, points)