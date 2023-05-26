list1 = ["hello", "take"]
list2 = ["dear", "sir"]


def join_lists(list1, list2):
    list1.extend(list2)


join_lists(list1, list2)
print (list1)
