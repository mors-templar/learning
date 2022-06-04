def linear_search(a_list, search_number):
    pos = -1
    i = 0
    while i < len(a_list)  and pos == -1:
        if a_list[i] == search_number:
            pos = i
        i = i + 1
    if pos == -1:
        print("not found")
    else:
        print("found at :", pos + 1)


search_num = int(input("please enter search num:"))
alist = [7, 9, 1, 4, 5]
linear_search(alist, search_num)
