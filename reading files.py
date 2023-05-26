newfile = open("filename.txt", 'w+')
# creates new file

instr = 'this will be inserted into the file'

newfile.write(instr)
# will add something to the file

import simplejson as json
import os

# open file and check whether it exists (and) check whether there is something inside the file
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    oldfile = open("./ages.json", 'r+')
    data = json.load(oldfile.read())
    # reads from oldfile variable and stores to data

# go to start
oldfile.seek()

# as data in the 'if statement' was in json we can keep using python function but if we need to output we will have
# to turn the python variable to json

