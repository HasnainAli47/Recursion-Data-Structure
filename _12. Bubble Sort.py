# Write function to do the bubble sort recursively.
# def BubbleSort(arr, slow, fast = 0):
#     if slow < 1:
#         return arr;
#     if fast < slow:
#         if arr[fast] > arr[fast + 1]:
#             temp = arr[fast]
#             arr[fast] = arr[fast+1]
#             arr[fast+1] = temp
#         return BubbleSort(arr, slow, fast + 1)
#     else:
#         return BubbleSort(arr, slow-1, 0)

# arr = [3,1,2,0,-1,-1,-2,5]
# ans = BubbleSort(arr, len(arr)-1)
# print(ans)
