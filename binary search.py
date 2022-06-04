#binary search

def binary_search ( list_1 , search_num):
    low = 0
    high = len(list_1) -1
    pos = -1
    while low <= high and pos == -1 :
        middle = (low + high)//2
        if list_1 [middle] == search_num:
            pos = middle
        elif list_1 [middle] < search_num :
            low = middle + 1
        else :
            high = middle - 1
    if pos == -1 :
        print ("not found")
    else :
        print ("found at pos:" , pos + 1)
    return list_1

list_1 = [2,5,9,11,13]         #:  assumed array already sorted
search_num = int(input("please enter search num"))
binary_search(list_1 ,search_num)
