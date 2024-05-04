# Write function to do the selection sort recursively

# def SelectionSort(arr, slow, fast, max):
#     if slow < 1:
#         return;
#     if fast < slow:
#         if arr[fast] > arr[max]:
#             SelectionSort(arr, slow, fast+1, fast)
#         else:
#             SelectionSort(arr, slow, fast+1, max)
#     else:
#         print(arr)
#         temp = arr[max]
#         arr[max] = arr[slow - 1]
#         arr[slow-1] = temp
#         SelectionSort(arr, slow-1, 0, 0)
    
    


# arr = [0, 4,2,3,1]
# ans = SelectionSort(arr, len(arr), 0, 0)
# print(ans)