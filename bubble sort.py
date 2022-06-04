list_1 = [3, 1, 9, -3]
def bubble_sort( list_1 ) :
    number_elements= len(list_1) - 1
    no_swaps_left = False
    while no_swaps_left == False:
        #no_swaps_left = True
        for j in range(0 , number_elements) :
            if list_1 [j] > list_1 [j] :
                temp = list_1 [ j ]
                list_1 [ j ] = list_1 [j + 1]
                list_1 [ j + 1] = temp
                no_swaps_left = False
        number_elements = number_elements - 1
        no_swaps_left = True
    print (list_1)
bubble_sort(list_1)