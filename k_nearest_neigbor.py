from sklearn.metrics.pairwise import manhattan_distances
from sklearn.neighbors import DistanceMetric
import numpy as np

squarelist = np.array([(6, 1), (7, 2), (8, 2), (9, 3), (6, 3), (7, 4), (5, 4)])
circlelist = np.array([(4, 4), (2, 5), (2, 8), (4, 6), (5, 5), (6, 5), (6, 6), (5, 7)])

point = np.array((6, 4))


def distance(point, list, label):
    newlist = []
    for elememt in list:
        newlist.append((manhattan_distance(point, elememt), label))
    return newlist


def manhattan_distance(a, b):
    return np.abs(a - b).sum()


def k_nearest_neigbor(point, list1, list2, number_of_points):
    first_list = distance(point, list1, "A")
    second_list = distance(point, list2, "B")
    combined_list = first_list + second_list
    sorted_by_first = sorted(combined_list, key=lambda tup: tup[0])
    new_list = sorted_by_first[:number_of_points]
    list_with_label = [x[1] for x in new_list ]
    list1_elements = list_with_label.count("A")
    list2_elements = list_with_label.count("B")
    print(list1_elements , list2_elements)


k_nearest_neigbor(point, squarelist, circlelist, 15)
