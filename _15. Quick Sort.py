# Write function to do QuickSort.
def QuickSort(arr, low, high):
    if low >= high:
        return arr;
    
    start = low
    end = high
    mid = start + (end - start) // 2
    pivote = arr[mid]
    while ( start <= end):
        while (arr[start] < pivote):
            start += 1 
        while (arr[end] > pivote):
            end -= 1
        
        if (start <= end):
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1
            print(arr, pivote, low, high)
   
    
    QuickSort(arr, low, end)
    return QuickSort(arr, start, high)

arr = [1,3,4,56,2]
print(QuickSort(arr, 0, len(arr)-1))
