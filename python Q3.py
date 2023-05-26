input_number = int(input("please enter the number to check"))


################################################################################
def check_numbers(num1, num2):
    if num1 == num2:
        return True
    else:
        return False


def slice_string(num):
    numTOstr = str(num)
    length_str = len(numTOstr)
    for x in numTOstr:
        index = int(x)
        start = numTOstr[index - 1:index]
        end = numTOstr[-index:length_str + 1 - index]
        if not check_numbers(start, end):
            return False
            break
        else:
            return True


#################################################################################
print(slice_string(input_number))
