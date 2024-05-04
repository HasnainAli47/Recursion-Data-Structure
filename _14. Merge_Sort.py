# Write a function to do merge sort recursively.
# Implement merge sort.
# def MergeSort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
    
#     left = MergeSort(arr[:mid])
#     right = MergeSort(arr[mid:])
    
#     return MergeArray(left, right)

# def MergeArray(left, right):
#     i = 0
#     j = 0
#     mix = []
#     while (i < len(left) and j < len(right)):
#         if left[i] < right[j]:
#             mix.append(left[i])
#             i += 1
#         else:
#             mix.append(right[j])
#             j += 1
#     mix.extend(left[i:])
#     mix.extend(right[j:])
            
#     return mix  

# arr = [3, 7, 2, 1, 9, 5, 8, 4, 6]
# print(MergeSort(arr))
