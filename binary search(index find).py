def binary_search(arr,key):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            left = mid+1
        else:
            right = mid-1
    return -1
arr = [2,3,4,9,10,15,23]
key = 15
result = binary_search(arr,key)
print(result)  #the result will be 5