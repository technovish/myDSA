def binarysearch(arr, target):

    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left+right) // 2
        if target == arr[mid]:
            return mid
        
        elif target > arr[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1

arr = [-10, 11, 100, 500, 2, -357, -13]
arr.sort()
target = -13
result = binarysearch(arr, target)
print(arr)
print(result)


