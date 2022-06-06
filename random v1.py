# print random numbers and store in array
import random

x = int(input("enter array start value"))
y = int(input("enter array end value"))
z = int(input("enter array termination value"))

rogue_reached = False
start_index = 1
end_index = int(z+1)
randarray = []

while rogue_reached == False:
    randarray.append( random.randint(x, y))
    if start_index == z:
        rogue_reached = True
    start_index = start_index + 1

print (randarray)