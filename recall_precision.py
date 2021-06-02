
f_o_and_h_o = [("A", "A"),("B", "A"), ("B", "B"), ("B", "B") , ("A", "B"), ("A", "B") , ("A", "A"), ("A", "A") , ("A", "A"), ("B" , "B") ]







def precandrecall(list, classes_list):
    for class_label in classes_list:
        tp = len([class_labelelement for class_labelelement in list if (class_labelelement[0] == class_label and class_labelelement[1] == class_label )])
        fp = len([class_labelelement for class_labelelement in list if (class_labelelement[0] != class_label and class_labelelement[1] == class_label )])
        fn = len([class_labelelement for class_labelelement in list if (class_labelelement[0] == class_label and class_labelelement[1] != class_label )])
        precision = tp/(tp+fp)
        recall = tp/(tp+fn)
        print(class_label, "precision is " , precision, "recall is " ,  recall)


precandrecall(f_o_and_h_o, ["A", "B"])