# Check if an array is sorted or not
def Array(arr, pointer = 0):
    if pointer >= len(arr)-1:
        return True
    return arr[pointer] <= arr[pointer + 1] and Array(arr, pointer+1)

arr = [1,11,13,32,453]
print("Array is sorted?", Array(arr))