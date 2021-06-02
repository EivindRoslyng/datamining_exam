#data = [["s", "b", "b", "s", "b", "s", "s", "s", "s", "b"],["s", "b", "s", "s", "s", "s", "b", "b", "b", "s"], ["b", "b", "s", "b", "b", "s", "s", "s", "b", "s"]]
#target = ["y", "y", "y", "y", "y", "y", "n", "n", "n", "n"]
import numpy as np
data = [["s", "s", "b", "yes"], ["b", "b", "b", "yes"  ], ["b", "s", "s", "yes"], ["s", "s", "b", "yes"],
         ["b", "s", "b", "yes"], ["s", "s", "s", "yes"] , ["s", "b", "s", "no"] , ["s", "b", "s", "no"],["b", "s", "s", "no"], ["s", "b", "b", "no"]]



def naivebayes(data, query, verifycontent):
    target = [element[-1] for element in data]
    target_values = list(set(target))
    target_percent_withoutlabel = [target.count(element) / len(target) for element in target_values]
    #listofvalue = [point for point in data if element  for element in list(set(target)) ]
    newlist = []
    for i in range(len(target_values)):
        newlist.append([point for point in data if point[-1] == target_values[i] ])

    anotherlist = []
    for i in range(len(list(target_values))):
        thirdlist = 1
        for j in range(len(query)):
            value = len([point for point in newlist[i] if point[j] ==  query[j]]) /len(newlist[i])
            thirdlist = value*thirdlist
        anotherlist.append(thirdlist)
    content = np.array(anotherlist * np.array(target_percent_withoutlabel))
    finalresult = list(zip(content , target_values))
    max_element = max(content)

    for element in list(finalresult):
        if element[0] == max_element:
            print("the one with the content is ",  element)




naivebayes(data, ["b","s", "b"], "buy")