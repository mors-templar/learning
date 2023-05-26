set1 = {10, 20, 30}
set2 = {20, 40, 50}


##########################
def unique_set(set1, set2):
    return set1.difference(set2)


##########################
print(unique_set(set1, set2))
