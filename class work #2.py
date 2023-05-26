count = 0
check = bool
for x in range(2, 1001):
    for num in range(2, 1001):
        if x % num == 0 and x != num:
            check = False

    if check == True:
        print (x)
        count = count + 1
    check = True
print("prime count is:", count+1)
