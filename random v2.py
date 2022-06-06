# print random numbers and store in array with validation
import random

x = int(input("enter array start value"))
y = int(input("enter array end value"))
z = int(input("enter array termination value"))
rogue_reached = False
start_index = 0
end_index = int(z+1)
randarray = []
if end_index >= y :
    print("termination value must be lower then", y-x)
    y = int(input())

def array_check(randomvalue):
    global randarray
    for count in range(len(randarray)):
        if randomvalue != randarray[x]:
            return
        else:
            return False


while rogue_reached == False:

    if start_index == end_index:
        rogue_reached = True
    random_value = random.randint(x, y)
    ac= array_check(random_value)
    if ac == True:
        randarray.append(random_value)
        start_index = start_index + 1


print (randarray)