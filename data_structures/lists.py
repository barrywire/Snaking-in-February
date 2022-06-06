import random
import math

randList = ["string", 1.234, 28]

oneToTen = list(range(1, 11))

randList = oneToTen + randList 

print('randList is a list of length: ', len(randList), 'with elements', randList)

# Using slice
first3 = randList[0:3]

for i in first3:
    print('{} : {}'.format(first3.index(i), i))
