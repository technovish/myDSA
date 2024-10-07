import array
import numpy as np

array2 = array.array('i', [1,2,3,5,6,7,9])
#print(np_array2[-1])

#another way array can be defined using other liberary
array3 = np.array([1,5,7,9,9,10])

#array insertion
array2.insert(0, 100)
array2.insert(2, 45)
#deleting element from array
array2.remove(45)


#linear search
def linearsearch(are, targt):
    for i in range(len(are)):
        if are[i] == targt:
            return i
    return -1
#print(linearsearch(array2, 45))

#array traversal
def traverse(ar):
    are = ar.tolist()
    for i in are:
        print(i)

traverse(array2)
