
from itertools import combinations
from itertools import chain


def generate (listofelement):
    new_list = []
    n = 0
    size_of_element = len(listofelement[0])+1
    for item in listofelement:
        list_of_unique = []
        n +=1
        for new_item in listofelement[n:]:
           list_of_unique.append(tuple(set.union(set(item), set(new_item))))
        new_list.append(list_of_unique)
    join = list(set([element for sublist in new_list for element in sublist if len(element) == size_of_element]))
    prunface = [element for element in join if (set(combinations(element, size_of_element-1)).issubset(set(listofelement))) ]
    print("generated doing join phase ",join)
    print("generated doing prun phase ", prunface)
    print("element which has been pruned ", [element for element in join if( (element) not in prunface)] )

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def prunerule(data):
    left_hand = data[0]
    right_hand = data[1]
    newlist = []
    for element in list(powerset(left_hand))[1:]:
        left_rule = list(element)
        right_rule = set(left_hand + right_hand) - set(left_rule)
        print(left_rule, "=>",  right_rule)









prunerule([["b", "c", "d"], ["e"]])

#generate([(1,4), (2,4), (1,2) ,(3,4)])

