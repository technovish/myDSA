from array import *

arr = array('i', [1,2,3])

arr.insert(2,9)
#print(arr)

def traverse(ar):
    are = ar.tolist()
    for i in are:
        print(i)


traverse(arr)