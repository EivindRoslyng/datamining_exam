
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from scipy.stats import entropy
data = [["littlefinger", "headline", "fateline", "passed exam"] , ["straight", "long", "invisible", "yes"], ["bent", "long", "invisible", "yes"],
        ["straight", "long", "deep", "no"] ,   ["straight", "long", "invisible", "no"],   ["straight", "long", "deep", "no"] ,   ["straight", "long", "invisible", "no"],
        ["straight", "long", "deep", "yes"] ,  ["bent", "long", "invisible", "no"] ,  ["bent", "short", "deep", "no"] ,["straight", "short", "invisible", "no"],
        ["bent", "short", "invisible", "no"],  ["straight", "short", "deep", "yes"]]

'''

def calent(data,target):
    con = list(zip(data, target))
    for elements in list(set(data)):
        listofelemets = [x for x in con  if x[0] == elements]
        target_likelihood = [len(target) / target.count(x) for x in list(set(target))]
        entropy(target_likelihood)


def decision_tree(content, root, rootsplit):
    data = content[1:]
    indexofvariable = content[0].index(root)
    newlist = []
    for datapoint in data:
        if datapoint[indexofvariable] != rootsplit:
            continue
        else:
            datapoint.remove(rootsplit)
            newlist.append(datapoint)

    target = [x[-1] for x in newlist]
    target_likelihood = [len(target)/target.count(x) for x in list(set(target))]
    entropy_of_target = entropy(target_likelihood)
    i = [ x.remove(x[-1]) for x in newlist ]
    for i in range(len(newlist[0])):
        elements = [x[i] for x in newlist]
        calent(elements, target)
decision_tree(data, "headline", "short" )


'''