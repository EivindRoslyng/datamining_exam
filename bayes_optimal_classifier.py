import numpy as np
classdis = np.array([0.5, 0.3 , 0.2])
plus0 = np.array([[0.6, 0.2, 0.9],[0.6, 0.6, 1], [0.6 , 0.6, 0]])
minus0 = np.array([[0.4, 0.8, 0.1], [0.4, 0.4, 0], [0.4,0.4, 1]])


def bayes_optimal(listplus, listminus, dis):
    n = 1
    for element in listplus:
        value = sum(element*dis)
        print("+O", n ,  value)
        n+= 1
    n = 1
    print()
    for element in listminus:
        value = sum(element * dis)
        print("-O", n, value)
        n += 1


bayes_optimal(plus0, minus0, classdis)