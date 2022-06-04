def insertionsort(a_list):
    for this_pointer in range(1, len(a_list)):
        temp = a_list[this_pointer]
        pointer = this_pointer - 1
        while a_list[pointer] > temp and pointer >= 0:
            a_list[pointer + 1] = a_list[pointer]
            pointer = pointer - 1
        a_list[pointer + 1] = temp
    return a_list


alist1 = [7, 9, 1, 4, 5, 8]
print("values in list before sorting :", alist1)
print("values in list after sorting are", insertionsort(alist1))
