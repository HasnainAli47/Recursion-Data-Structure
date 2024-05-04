# Write a recursive function to perform a binary search on a sorted list of integers.
# The function should return the index of the target element if it's present in the list, otherwise return -1.

def BinarySearch(arr, target, left, right):
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySearch(arr, target, left, mid - 1)
    return BinarySearch(arr, target, mid + 1, right)
    
    
arr = [1,2,3,4,5,6]
print("3 is present at index ", BinarySearch(arr, 13, 0, len(arr)-1))
