import array
import numpy as np

array1 = array.array('i',[1,10,12,14,15,2,3,4,5,6,7,8,9])

def traverse(ar):
    lst = ar.tolist()
    for i in lst:
        print(i)

traverse(array1)