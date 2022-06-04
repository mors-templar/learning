# write a recursive function to calculate sum of number up to a value
def  sum(number):
    if number == 1:
        return 1
    else:
        return number + sum(number-1)

number = int(input("enter number"))
print(sum(number))
